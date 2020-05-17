from typing import Tuple
import math

class Coordinates():
  def __init__(self,c: Tuple[float,float,float]):
    self._x = int(c[0])
    self._y = int(c[1])
    self._z = int(c[2])
  def x(self):
    return self._x
  def y(self):
    return self._y
  def z(self):
    return self._z

# This is like tradition coordinates where 1 unit represents 1 block
class BlockCoordinates(Coordinates):

# 16x16 block Chunk
class ChunkCoordinates(Coordinates):

# 32x32 chunk Region
class RegionCoordinates(Coordinates):
  
  

# This takes MinecraftCoordinates
class RectangularBorder():
  def __init__(self, x_1, x_2, z_1, z_2):
    self.left = min(x_1, x_2)
    self.right = max(x_1, x_2)
    self.top = max(z_1, z_2)
    self.bottom = min(z_1, z_2)
  def 

class ConvertCoordinates():
  # Used to convert units
  def block_to_chunk(self, chunk: BlockCoordinates) -> ChunkCoordinates:
    chunk_x = math.floor(chunk.x()/16)
    chunk_y = math.floor(chunk.y()/16)
    chunk_z = math.floor(chunk.z()/16)
    return BlockCoordinates(
  def region_borders(region: RegionCoordinates) -> BlockCoordinates: