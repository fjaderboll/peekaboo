import gc
import utime
from machine import Pin, SoftI2C

import PicoRobotics
from buzzer import Buzzer
from buzzer_sounds import Sounds
from ultrasonic import Ultrasonic

from head import Head
from body import Body

print('Starting...')

# === init variables ===
pirPin = Pin(19, Pin.IN)
ledPin = Pin("LED", Pin.OUT)

board = PicoRobotics.KitronikPicoRobotics() # uses i2c1
buzzer = Buzzer(18)
sounds = Sounds(buzzer)
i2c0 = SoftI2C(scl=Pin(17), sda=Pin(16), freq=100_000)
utime.sleep(1)

sensor_front = Ultrasonic(11, 15, 'Front')
sensor_left  = Ultrasonic(10, 14, 'Left')
sensor_right = Ultrasonic(7, 13, 'Right')
sensor_back  = Ultrasonic(6, 12, 'Back')

head = Head(board, i2c0, servo_yaw=7, servo_pitch=8)
body = Body(board, head, sensor_front, sensor_left, sensor_right, sensor_back)

# === end init variables ===

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

# === main ===
pirPin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pir_irq)

print('Started')
sounds.play_startup()

last_found_someone = False
last_print_time = 0

start_time = utime.ticks_ms()
start_hold = True
try:
    while True:
        # beginning
        if start_hold:
            start_hold = (utime.ticks_diff(utime.ticks_ms(), start_time) < 7000)
            if not start_hold:
                sounds.play_startup_end()

        # move stuff
        head.update()
        body.update(start_hold)

        # did we find someone?
        if head.has_found_someone():
            if not last_found_someone:
                print('Found someone')
                sounds.play_found_someone()
                last_found_someone = True
        else:
            if last_found_someone:
                print('Lost someone')
                sounds.play_lost_someone()
                last_found_someone = False

        # debug print state
        if utime.ticks_diff(utime.ticks_ms(), last_print_time) > 1000:
            head.print_state(print_camera=False)
            body.print_state()
            last_print_time = utime.ticks_ms()
        
        # idle a little
        utime.sleep_ms(100)
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    print('Shutting down')
    body.stop_motors()
    buzzer.silent()
