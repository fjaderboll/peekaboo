#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

servoBottom = 7
servoTop = 8

# servo both
for degrees in range(60, 120, 3):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(30)
for degrees in range(120, 90, -1):
    board.servoWrite(servoBottom, degrees)
    board.servoWrite(servoTop, degrees)
    utime.sleep_ms(10)
