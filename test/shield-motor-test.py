#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime

board = PicoRobotics.KitronikPicoRobotics()
directions = ['f', 'r']

# one by one
for motor in range(2):
    for direction in directions:
        for speed in range(100):
            board.motorOn(motor+1, direction, speed)
            utime.sleep_ms(20)
        for speed in range(100):
            board.motorOn(motor+1, direction, 100-speed) #ramp down
            utime.sleep_ms(20)
    board.motorOff(motor+1)

# both
for direction in directions:
    for speed in [20, 50, 100, 50, 20]:
        for motor in range(2):
            board.motorOn(motor+1, direction, speed)
        utime.sleep_ms(1000)
board.motorOff(1)
board.motorOff(2)
