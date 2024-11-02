#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

# servo 1
for degrees in range(0, 130, 3):
    board.servoWrite(1, degrees)
    utime.sleep_ms(30)
for degrees in range(130, 65, -1):
    board.servoWrite(1, degrees)
    utime.sleep_ms(10)

# servo 2
for degrees in range(0, 140, 3):
    board.servoWrite(2, degrees)
    utime.sleep_ms(30)
for degrees in range(140, 65, -1):
    board.servoWrite(2, degrees)
    utime.sleep_ms(10)

# servo 1+2
for degrees in range(0, 140, 3):
    board.servoWrite(1, degrees)
    board.servoWrite(2, degrees)
    utime.sleep_ms(30)
for degrees in range(140, 65, -1):
    board.servoWrite(1, degrees)
    board.servoWrite(2, degrees)
    utime.sleep_ms(10)
