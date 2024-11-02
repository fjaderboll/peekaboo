from machine import I2C, Pin
import utime
from amg88xx import AMG88XX

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100_000)

sensor = AMG88XX(i2c)
utime.sleep(1)

print('AMG88XX, 8x8 pixel heat camera, temperatures in Celsius:')
while True:
    sensor.refresh()

    for row in range(8):
        for col in range(8):
            temp = sensor[row, col]
            print('{:3d}'.format(temp), end='')
        print()
    
    utime.sleep(0.4)
    for row in range(8):
        print(LINE_UP, end=LINE_CLEAR)
