# amg_test.py Basic test of AMG8833 sensor

# Released under the MIT licence.
# Copyright (c) Peter Hinch 2019

import machine
import utime
import time
from amg88xx import AMG88XX


i2c = machine.I2C(0)
print('I2C scan: ',i2c.scan())
time.sleep(1)
sensor = AMG88XX(i2c)
time.sleep(1)
while True:
    utime.sleep(0.2)
    sensor.refresh()
    for row in range(8):
        print()
        for col in range(8):
            print('{:4d}'.format(sensor[row, col]), end='')
