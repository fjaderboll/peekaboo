import utime
import random

import PicoRobotics
from buzzer import Buzzer

board = PicoRobotics.KitronikPicoRobotics()
buzzer = Buzzer(18)

servoBottom = 7
servoTop = 8

def move_head():
    # servo both
    for degrees in range(60, 120, 3):
        board.servoWrite(servoBottom, degrees)
        board.servoWrite(servoTop, degrees)
        utime.sleep_ms(30)
    for degrees in range(120, 90, -1):
        board.servoWrite(servoBottom, degrees)
        board.servoWrite(servoTop, degrees)
        utime.sleep_ms(10)

def play_startup_sound():
    # random tones
    min_msg_len = 2
    max_msg_len = 5
    random_tones = []
    for _ in range(random.randint(min_msg_len, max_msg_len)):
        random_tone = random.choice(list(buzzer.tones.keys()))
        random_tones.append(random_tone)
    #print(random_tones)
    buzzer.play_song(random_tones, tone_delay=0.2)

play_startup_sound()
move_head()
