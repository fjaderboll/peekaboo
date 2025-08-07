#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

servoBottom = 7
servoTop = 8

bottomMin = 30
bottomMiddle = 90
bottomMax = 150
topMin = 60
topMiddle = 90
topMax = 110

# servo bottom
for degrees in range(bottomMin, bottomMax, 3):
    board.servoWrite(servoBottom, degrees)
    utime.sleep_ms(30)
for degrees in range(bottomMax, bottomMiddle, -1):
    board.servoWrite(servoBottom, degrees)
    utime.sleep_ms(10)

# servo top
for degrees in range(topMin, topMax, 3):
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(30)
for degrees in range(topMax, topMiddle, -1):
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(10)

# servo both
for degrees in range(max(bottomMin, topMin), min(bottomMax, topMax), 3):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(30)
for degrees in range(min(bottomMax, topMax), (bottomMiddle+topMiddle)//2, -1):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(10)
