import gc
import utime
import random
from machine import Pin

import PicoRobotics
from buzzer import Buzzer
from ultrasonic import Ultrasonic

# --- init variables ---
pirPin = Pin(19, Pin.IN)
ledPin = Pin("LED", Pin.OUT)

board = PicoRobotics.KitronikPicoRobotics()
buzzer = Buzzer(18)

servoBottom = 7
servoTop = 8

ultrasonics = [
    Ultrasonic(11, 15, 'Front'),
    Ultrasonic(10, 14, 'Left'),
    Ultrasonic(7, 13, 'Right'),
    Ultrasonic(6, 12, 'Back'),
]
# --- ---

def mem():
  gc.collect()
  free = gc.mem_free()
  alloc = gc.mem_alloc()
  total = free + alloc
  print(f'Memory used: {alloc/total*100:.1f}%')

def pir_irq(pin):
    if pin.value():
        print('PIR detected motion')
    else:
        print('PIR motion stopped')
    ledPin.value(pin.value())

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

def play_random_sound(min_tones=2, max_tones=5):
    random_tones = []
    for _ in range(random.randint(min_tones, max_tones)):
        random_tone = random.choice(list(buzzer.tones.keys()))
        random_tones.append(random_tone)
    #print(random_tones)
    buzzer.play_song(random_tones, tone_delay=0.2)

pirPin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pir_irq)

play_random_sound()
move_head()

us_triggers = {}
while True:
    for us in ultrasonics:
        d = us.measure_distance()
        is_close = 0.1 < d and d < 5  # skip 0 values
        if is_close and not us_triggers.get(us.get_name(), False):
            play_random_sound(1, 2)
            print(f'Proximity {us.get_name()}: {d:.1f} cm')
        us_triggers[us.get_name()] = is_close
    utime.sleep_ms(1000)
