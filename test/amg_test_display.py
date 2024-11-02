from machine import I2C, Pin
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

def normalize(low, high):
    norm = [[0 for i in range(8)] for j in range(8)]
    for row in range(8):
        for col in range(8):
            norm[row][col] = (heat[row, col] - low)/(high - low)
    
    return norm

def find_weight_center(arr):
    wx = 0
    wy = 0
    s = 0
    for x in range(8):
        for y in range(8):
            v = arr[x][y]
            if v > 0.9:
                wx += v * x
                wy += v * y
                s  += v
    
    if s == 0:
        return (0, 0)
    return (wx / s, wy / s)

def draw_debug():
    s = 10
    ox = 0
    oy = 10
    fps = 0
    
    while True:
        time.sleep(0.1)
        start_time = utime.ticks_ms()
        heat.refresh()
        
        display.fill(0)
        #display.rect(ox, oy, 8*s+2, 8*s+2, 0, f=True)
        display.rect(ox, oy, 8*s+2, 8*s+2, 1, f=False)
        display.text('AMG display test', 0, 0, 1)
        
        (low, high) = find_low_high()
        temp_norm = normalize(low, high)
        
        # heat display
        color = 1
        for row in range(8):
            for col in range(8):
                area = temp_norm[row][col] * s * s
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
        
        # stats
        display.text("Range:", ox + 8*s+2+1, 10, 1)
        display.text(f"{low}-{high}", ox + 8*s+2+1, 20, 1)
        display.text("FPS:", ox + 8*s+2+1, 30, 1)
        display.text(f"{int(fps)}", ox + 8*s+2+1, 40, 1)
        
        # heat center
        (wx, wy) = find_weight_center(temp_norm)
        x = int(ox + wx*s+1)
        y = int(oy + wy*s+1)
        display.ellipse(x, y, 10, 10, 0)
        display.ellipse(x, y, 9, 9, 1)
        #print(f"x={x} y={y} wx={wx} wy={wy}")
        
        # eyes
        display.ellipse(16, 110, 16, 16, 1)
        display.ellipse(64, 110, 16, 16, 1)
        dx = int((wx-4)/4*8)
        dy = int((wy-4)/4*8)
        display.ellipse(16+dx, 110+dy, 8, 8, 1, True)
        display.ellipse(64+dx, 110+dy, 8, 8, 1, True)
        
        display.show()
        
        elapsed_time = utime.ticks_ms() - start_time
        fps = 1000 / elapsed_time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
#print('I2C scan: ',i2c.scan())
#time.sleep(1)
heat = AMG88XX(i2c) # , addr=105
time.sleep(0.1)
display = SH1107_I2C(128, 128, i2c, address=60, rotate=0, delay_ms=800)
time.sleep(0.1)

display.fill(0)
display.text('AMG display test', 0, 0, 1)
display.show()
time.sleep(0.1)

draw_debug()
