from machine import I2C, Pin
import utime

import PicoRobotics
from amg88xx import AMG88XX

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

def find_low_high():
    low = 100
    high = 0
    for row in range(8):
        for col in range(8):
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
    
    (rx, ry) = ((wx / s - 4) / 4, (wy / s - 4) / 4)
    return (-ry, rx)  # consider sensor rotation

def render_pixel(v):
    chars = ' .:oO@'
    i = int(v*10/2)
    return chars[i]

def update_head_position():
    board.servoWrite(1, yaw)
    board.servoWrite(2, pitch)

def move_head(wx, wy):
    global yaw, pitch

    yaw = max(0, min(130, yaw + wx * 10))
    pitch = max(60, min(130, pitch + wy * 10))
    update_head_position()

board = PicoRobotics.KitronikPicoRobotics() # usex i2c0

i2c1 = I2C(1, sda=Pin(2), scl=Pin(3), freq=100_000)
heat = AMG88XX(i2c1)
utime.sleep(1)

yaw = 65
pitch = 110
update_head_position()

print('AMG88XX, 8x8 pixel heat camera, temperatures in Celsius:')
while True:
    heat.refresh()
    (low, high) = find_low_high()
    temp_norm = normalize(low, high)
    (wx, wy) = find_weight_center(temp_norm)

    for row in range(8):
        for col in range(7, -1, -1):
            #temp = heat[row, col]
            #print(' {:3d}'.format(temp), end='')
            v = temp_norm[row][col]
            s = render_pixel(v)
            print(s, end=' ')
        print()
    
    print('wx: {:.1f} wy: {:.1f}'.format(wx, wy))

    utime.sleep(0.2)
    move_head(wx, wy)

    for row in range(8+1):
        print(LINE_UP, end=LINE_CLEAR)
