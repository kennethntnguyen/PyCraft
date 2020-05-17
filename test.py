import time
class fillException(Exception):
  pass

def fill_string(from_x: int, from_y: int, from_z: int, to_x: int, to_y: int, to_z: int, block: str = None, mode: str = None) -> str:
  if  block == None:
    raise fillException('No block type defined. Example: "minecraft:stone_bricks". A block ID number can be used as well.')
  mode_arguments = ['destroy', 'hollow', 'keep', 'outline', 'replace']
  if mode in mode_arguments:
    return 'fill ' + str(from_x) + ' ' + str(from_y) + ' ' + str(from_z) + ' ' + str(to_x) + ' ' + str(to_y) + ' ' + str(to_z) + ' ' + block + ' ' + mode
    time.sleep(0.05)
  elif mode == None:
    return 'fill ' + str(from_x) + ' ' + str(from_y) + ' ' + str(from_z) + ' ' + str(to_x) + ' ' + str(to_y) + ' ' + str(to_z) + ' ' + block
  else:
    raise fillException('Invalid mode input. Valid modes include: destroy, hollow, keep, outline & replace.')