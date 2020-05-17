from pycraft import ServerTools as st
import numpy as np
import time

#horizontal_direction = 'x'
#vertical_direction = 

pcr = st()
pcr.login()

x = 83

from_y = 105
to_y = 63

start_z = -446

time.sleep(3)

for i in range(abs(from_y-to_y) + 1):
  pcr.command('fill ' + str(x) + ' ' + str(from_y - i) + ' ' + str(start_z + i) + ' ' + str(x) + ' ' + str(from_y - i) + ' ' + str(start_z + i) + ' minecraft:air')
  time.sleep(0.1)

pcr.logout()
