from machine import I2C, Pin, SoftI2C
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

def update_head_position(new_yaw=0, new_pitch=0):
    global yaw, pitch

    if new_yaw != yaw:
        yaw = new_yaw
        board.servoWrite(7, yaw)
    if new_pitch != pitch:
        pitch = new_pitch
        board.servoWrite(8, pitch)

def move_head(wx, wy):
    step_size = 10
    new_yaw = max(0, min(130, yaw + wx * step_size))
    new_pitch = max(60, min(130, pitch + wy * step_size))
    update_head_position(new_yaw, new_pitch)

board = PicoRobotics.KitronikPicoRobotics() # usex i2c1

i2c0 = SoftI2C(scl=Pin(17), sda=Pin(16), freq=100_000)
heat = AMG88XX(i2c0)
utime.sleep(1)

yaw = 0
pitch = 0
update_head_position(65, 110)

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
