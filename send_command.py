from pycraft import RconTools

def main():
  with RconTools() as rt:
    rt.command('say test')

if __name__== '__main__': main()