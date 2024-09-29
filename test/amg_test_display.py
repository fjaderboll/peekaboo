# amg_test.py Basic test of AMG8833 sensor

# Released under the MIT licence.
# Copyright (c) Peter Hinch 2019

from machine import I2C
import utime
import time
from amg88xx import AMG88XX
from sh1107 import SH1107_I2C

i2c = I2C(0)
heat = AMG88XX(i2c)
display = SH1107_I2C(128, 128, i2c, address=60, rotate=0, delay_ms=800)
time.sleep(0.5)

display.fill(0)
display.text('AMG display test', 0, 0, 1)
display.show()

time.sleep(1)

low = 20
high = 30
s = 10
while True:
    time.sleep(0.1)
    heat.refresh()
    
    #display.fill(0)
    display.rect(0, 0, 8*s, 8*s, 0, f=True)
    c = 1
    for row in range(8):
        print()
        for col in range(8):
            #print('{:4d}'.format(heat[row, col]), end='')
            temp = heat[row, col]
            o = int((1-(temp - low)/(high - low))*s/2)
            display.rect(row*s+o, col*s+o, s-2*o, s-2*o, c, f=True)
    
    display.show()
