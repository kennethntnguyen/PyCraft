from MCRcon.mcrcon import MCRcon
import sys
import os
import time

# Uses 'server.properties' to log into MC Rcon, if you want to input login information yourself and use CLI use MCRcon from repo 'Uncaught-Exceptions/MCRcon'
# Offers various tools for automating rcon tasks and parsing various Minecraft player and world information files created by the server
class RconTools(MCRcon):
    def __init__(self, server_properties_filename = 'server.properties'):
        self._server_properties = self.server_properties_to_dict(server_properties_filename)
        self._server_ip = self._server_properties['server-ip']
        self._rcon_password = self._server_properties['rcon.password']
        self._rcon_port = self._server_properties['rcon.port']
        self._rcon_session = MCRcon(self._server_ip, self._rcon_password, self._rcon_port)
    def __enter__(self):
        self._rcon_session.connect()
        return self
    def __exit__(self, type, value, tb):
        self._rcon_session.disconnect()

    def get_rcon_session(self):
        return self._rcon_session
    def get_server_properties(self):
        return self._server_properties
    def get_server_ip(self):
        return self._server_ip
    def get_rcon_password(self):
        return self._rcon_password
    def get_rcon_port(self):
        return self._rcon_port
    def login(self):
        self._rcon_session.connect()
    def logout(self):
        self._rcon_session.disconnect()

    # Pull server informations from 'server.properties' file
    def server_properties_to_dict(self, server_properties_filename):
        # Loads and splits Minecraft server.properties values into a dictionary
        file_path = None
        file_exists = False
        server_properties = {}
        if os.path.exists(server_properties_filename):
            file_path = server_properties_filename
            file_exists = True
        elif os.path.exists(os.path.join(os.pardir, server_properties_filename)):
            file_path = os.path.join(os.pardir, server_properties_filename)
            file_exists = True
        else:
            print("Error: File does not appear to exist. Make sure 'server.properties' file is named correctly or the correct name is passed during instantiating.")
            raise FileNotFoundError
        if file_exists:
            try:
                with open(file_path, 'r') as f:
                    server_properties = f.read().split('\n')
                    properties = ['=' in value for value in server_properties]
                    properties = [server_properties[i]
                        for i in range(0, len(properties)) if properties[i]]
                    server_properties = dict([props.split('=') for props in properties])
                    # Converts port numbers from strings to integers since rcon uses integers for these values
                    for d in server_properties:
                        if(d in ['server-port', 'rcon.port', 'query.port']):
                            server_properties[d] = int(server_properties[d])
            except IOError:
                print('There was an IOError.')
        return server_properties
    
    # Command function that doesn't require you to type '/' before each command
    def command(self, rcon_command: str):
        return self._rcon_session.command('/' +  rcon_command)
    
    # Shut down respective server via rcon
    def stop_server(self, delay: int = 10):
        # Message users that server is shutting down in 10 seconds
        self.command('say Server shutting down in 10 seconds... Saving world.')
        # Saves world and gets confirmation
        confirm_save = self.command('save-all')

        # Starts shutdown sequence if save was successful
        if 'Saved the game' in confirm_save:
            for i in range(delay,0,-1):
                resp = self.command('say ' + str(i) + '...')
                time.sleep(1)
            self.command('Bye Bye!')
            time.sleep(0.5)
            self.command('stop')
        else:
            print('Save was not successful.\n')
            print('Rcon Response: ' + str(confirm_save))