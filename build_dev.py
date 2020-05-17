import time
import numpy as np

# Exceptions
class fillException(Exception):
  pass

# Algorithm notes
# If building in z direction then fix x and vice versa
# Stair direction can either be +z,-z,+x,-x
# Split up width of stairs to be width 1 so that we can choose material scheme as well
#

# Algorithm
# 1. Find out building direction
# 2. Fix correct axis (if building direction is x then left and right edges correspond to z coordinates)
# 3. Split up stair width by unit and know the length
# 4. 


# Example Input
taper = True
taper_scheme = np.array([3,2,1,2,3])
stair_direction = '-z'
start_coordinate = -403
left_edge = 83
right_edge = 83
material = ['minecraft:stone_bricks']
start_y = 62
end_y = 100


#Part of alg
taper_n = len(np.array([3,2,1,2,3]))


def __y_incrementor(int: start_y, int: end_y) -> int:
  if start_y-end_y < 0: # Start lower and end higher
    return 1 # Build stairs upwards
  elif 0 < start_y - end_y: # Start higher and end lower
    return -1 # Build stairs downwards
  else:
    print('These coordinates do not represent stairs. Coordinate y is fixed and does not change.')
    return 0

def constructBuildArray(str: stair_direction, )

def __direction_incrementor(str: stair_direction) -> int:
  n = len(stair_direction)
  if n == 2:
  elif  n == 1 and stair_direction is in ['x','y','z']: # No polarity must means that it is in the positive direction

def buildStairs(str: stair_direction, int: start, int: left_edge, int: right_edge, int: start_height, int: end_height, list: material):
  # Input validation
  n = len(stair_direction)
  if n == 2:
    if stair_direction == '+x':
      # left_edge and right_edge correspond to z and start_coordinate corresponds to x with positive increments from __direction_incrementor
    elif stair_direction == '-x':
      # left_edge and right_edge correspond to z and start_coordinate corresponds to x with negative increments from __direction_incrementor
    elif stair_direction == '+z':
      # left_edge and right_edge correspond to x and start_coordinate corresponds to z with positive increments from __direction_incrementor
    elif stair_direction == '-z':
      # left_edge and right_edge corresponds to x and start_coordinate cooresponds to z with negative increments from __direction_incrementor
    else:
      print('Incorrect stair direction. Should be one of the following: +x,-x,+z,-z.')
  elif  n == 1 and stair_direction is in ['x','y','z']: # No polarity must means that it is in the positive direction
  else:
  
  
  delta_height = (abs(start_y-end_y) + 1) # The total height of the stairs


if(taper == True and taper_n < delta_y ):
  x_i = np.array(np.ones(delta_y)*5,'int')
  y_i = np.arange(delta_y)
  y_i = np.array_split(y_i, taper_n)
  for t in taper_scheme:
    for i in range(1,t+1):
      
# Helper function to create fill command string
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