from hcsr04 import HCSR04
from time import sleep

class Ultrasonic:

    def __init__(self, trigger_pin, receiver_pin, name):
        self.sensor = HCSR04(trigger_pin=trigger_pin, echo_pin=receiver_pin, echo_timeout_us=10000)
        self.name = name

    def get_name(self):
        return self.name
    
    def measure_distance(self):
        self.last_distance = self.sensor.distance_cm()
        return self.last_distance

    def last_distance(self):
        return self.last_distance

sensors = [
    Ultrasonic(11, 15, 'Front'),
    Ultrasonic(10, 14, 'Left'),
    Ultrasonic(7, 13, 'Right'),
    Ultrasonic(6, 12, 'Back'),
]

while True:
    for sensor in sensors:
        print(f'{sensor.get_name()}: {sensor.measure_distance():.1f} cm', end='   ')
    print()
    sleep(1)
