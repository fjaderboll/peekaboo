# amg_test.py Basic test of AMG8833 sensor

# Released under the MIT licence.
# Copyright (c) Peter Hinch 2019

from machine import I2C
import time
from sh1107 import SH1107_I2C

i2c = I2C(0)
display = SH1107_I2C(128, 128, i2c, address=60, rotate=0, delay_ms=200)
time.sleep(0.5)

display.fill(0)
display.text('Amellia', 0, 0, 1)
display.text('God morgon!', 10, 10, 1)
display.rect(20, 20, 20, 20, 1, f=False)
display.show()

time.sleep(1)
