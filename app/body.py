import utime

from ultrasonic import Ultrasonic

class Body:
    def __init__(self, sensor_front: Ultrasonic, sensor_left: Ultrasonic, sensor_right: Ultrasonic, sensor_back: Ultrasonic):
        self.sensor_update_interval = 500
        self.last_update_time = 0
        
        self.sensor_front = sensor_front
        self.sensor_left  = sensor_left
        self.sensor_right = sensor_right
        self.sensor_back  = sensor_back
        self.sensors = [sensor_front, sensor_left, sensor_right, sensor_back]
        self.distances = [0, 0, 0, 0]
        self.proximity_threshold = 5

    def get_distances(self):
        return [sensor.get_last_distance() for sensor in self.sensors]

    def print_state(self):
        for sensor in self.sensors:
            print(f'{sensor.get_name()}: {sensor.get_last_distance():.1f} cm', end=' ')
        print()

    def update(self, stand_still: bool = False):
        if utime.ticks_diff(utime.ticks_ms(), self.last_update_time) > self.sensor_update_interval:
            for i, sensor in enumerate(self.sensors):
                distance = sensor.measure_distance()
                self.distances[i] = distance
            
            self.last_update_time = utime.ticks_ms()
