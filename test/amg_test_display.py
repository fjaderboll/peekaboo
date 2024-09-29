# amg_test.py Basic test of AMG8833 sensor

# Released under the MIT licence.
# Copyright (c) Peter Hinch 2019

from machine import I2C
import utime
import time
import math
from amg88xx import AMG88XX
from sh1107 import SH1107_I2C

def find_low_high():
    low = 100
    high = 0
    for row in range(8):
        for col in range(8):
            #print('{:4d}'.format(heat[row, col]), end='')
            temp = heat[row, col]
            if temp < low:
                low = temp
            if temp > high:
                high = temp
    
    if low == high:
        high += 1
    
    return (low, high)

def draw_debug():
    s = 10
    ox = 10
    oy = 10
    
    while True:
        time.sleep(0.1)
        heat.refresh()
        
        #display.fill(0)
        display.rect(ox, oy, 8*s+2, 8*s+2, 0, f=True)
        display.rect(ox, oy, 8*s+2, 8*s+2, 1, f=False)
        (low, high) = find_low_high()
        
        color = 1
        for row in range(8):
            for col in range(8):
                temp = heat[row, col]
                kvot = (temp - low)/(high - low)
                area = kvot * s * s
                side = math.sqrt(area)
                p = side - int(side)
                if p < 0.33:
                    w = h = math.floor(side)
                elif p > 0.66:
                    w = h = math.ceil(side)
                else:
                    w = math.floor(side)
                    h = math.ceil(side)
                
                if w > 0 and h > 0:
                    display.rect(ox + 1 + row*s + int((s-w)/2), oy + 1 + col*s + int((s-h)/2), w, h, color, f=True)
        
        display.rect(0, oy + 8*s+2+1, 128, 10, 0, f=True)
        display.text(f"Range: {low}-{high} C", 0, oy + 8*s+2+1, 1)
        display.show()

i2c = I2C(0)
heat = AMG88XX(i2c)
display = SH1107_I2C(128, 128, i2c, address=60, rotate=0, delay_ms=800)
time.sleep(0.5)

display.fill(0)
display.text('AMG display test', 0, 0, 1)
display.show()
time.sleep(1)

draw_debug()
