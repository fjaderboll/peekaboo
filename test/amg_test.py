from machine import I2C, Pin
from machine import SoftI2C
import utime
from amg88xx import AMG88XX

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

#i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=100_000)
i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=100_000)

sensor = AMG88XX(i2c, skip_scan=True) # i2c device: 105 / 0x69
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
