from hcsr04 import HCSR04

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
