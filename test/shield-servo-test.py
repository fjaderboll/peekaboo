#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

servoBottom = 7
servoTop = 8

# servo bottom
for degrees in range(0, 130, 3):
    board.servoWrite(servoBottom, degrees)
    utime.sleep_ms(30)
for degrees in range(130, 65, -1):
    board.servoWrite(servoBottom, degrees)
    utime.sleep_ms(10)

# servo top
for degrees in range(0, 140, 3):
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(30)
for degrees in range(140, 65, -1):
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(10)

# servo both
for degrees in range(0, 140, 3):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(30)
for degrees in range(140, 65, -1):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(10)
