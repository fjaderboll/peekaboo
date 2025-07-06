from hcsr04 import HCSR04
from collections import deque

class Ultrasonic:

    def __init__(self, trigger_pin, receiver_pin, name):
        self.sensor = HCSR04(trigger_pin=trigger_pin, echo_pin=receiver_pin, echo_timeout_us=10000)
        self.name = name
        self.distances: deque[float] = deque([], 5)

    def get_name(self):
        return self.name
    
    def measure_distance(self):
        distance = self.sensor.distance_cm()
        self.distances.append(distance)
        return distance

    def get_last_distance(self):
        if len(self.distances) == 0:
            return 0
        else:
            return self.distances[-1]
    
    def get_calibrated_distance(self):
        if len(self.distances) == 0:
            return 0
        else:
            # return median from self.distances
            ds = sorted(list(self.distances)) # type: ignore
            if len(ds) % 2 == 1:
                return ds[len(ds) // 2]
            else:
                return (ds[len(ds) // 2 - 1] + ds[len(ds) // 2]) / 2

            #sum = 0
            #for d in self.distances:
            #    sum += d
            #return sum / len(self.distances)
