from machine import Pin, SoftI2C
import utime

import PicoRobotics
from head import Head

board = PicoRobotics.KitronikPicoRobotics() # uses i2c1
i2c0 = SoftI2C(scl=Pin(17), sda=Pin(16), freq=100_000)
utime.sleep(1)

head = Head(board, i2c0, servo_yaw=7, servo_pitch=8)

print('AMG88XX, 8x8 pixel heat camera, temperatures in Celsius:')
while True:
    if head.update():
        head.print_state(use_numbers=True)
    utime.sleep_ms(10)
