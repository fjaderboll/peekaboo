import utime

from PicoRobotics import KitronikPicoRobotics
from ultrasonic import Ultrasonic
from head import Head

class Body:
    DIRECTION_FORWARD: str = 'r'
    DIRECTION_BACKWARD: str = 'f'
    MOTOR_LEFT: int = 1
    MOTOR_RIGHT: int = 2

    def __init__(self, board: KitronikPicoRobotics, head: Head, sensor_front: Ultrasonic, sensor_left: Ultrasonic, sensor_right: Ultrasonic, sensor_back: Ultrasonic):
        self.board = board
        self.head = head
        self.sensor_front = sensor_front
        self.sensor_left  = sensor_left
        self.sensor_right = sensor_right
        self.sensor_back  = sensor_back
        
        self.sensors = [sensor_front, sensor_left, sensor_right, sensor_back]
        #self.distances: deque[float] = [None, None, None, None]
        self.proximity_threshold = 5
        self.sensor_update_interval = 500
        self.last_update_time = 0

        self.angle = 0
        self.speed = 0
        self.last_speed = -1
        self.last_angle = -1

    def get_distances(self):
        return [sensor.get_last_distance() for sensor in self.sensors]

    def print_state(self):
        for sensor in self.sensors:
            print(f'{sensor.get_name()}: {sensor.get_last_distance():.1f} cm', end=' ')
        print()
    
    def read_sensors(self):
        for i, sensor in enumerate(self.sensors):
            sensor.measure_distance()
    
    def get_safe_speed(self, speed):
        min_speed = 20 # below this the motor doesn't move
        max_speed = 100
        return max(min_speed, min(speed, max_speed))

    def calculate_movement(self, stand_still: bool = False):
        if stand_still:
            self.speed = 0
            self.angle = 0
        elif self.head.has_found_someone():
            self.speed = 0
            self.angle = self.head.get_direction_angle()
        else:
            distance_front = self.sensor_front.get_calibrated_distance()
            distance_left  = self.sensor_left.get_calibrated_distance()
            distance_right = self.sensor_right.get_calibrated_distance()
            distance_back  = self.sensor_back.get_calibrated_distance()
            head_angle = self.head.get_direction_angle()

            if distance_front < 5 and distance_back > 10: # move backward
                print('Body: back')
                self.speed = 30
                self.angle = 180 + (20 if distance_left < distance_right else -20)
            if distance_front < 10: # turn on the spot
                print('Body: turn on the spot')
                self.speed = 0
                self.angle = 30 * (1 if head_angle > 0 else -1)
            else: # move forward against the head angle but stay away from obstacles
                print('Body: move forward')
                df = min(1, distance_front / 100)
                dl = min(1, distance_left / 100)
                dr = min(1, distance_right / 100)
                self.speed = self.get_safe_speed(df * 50 + dl * 25 + dr * 25)
                self.angle = head_angle * 0.5 - dl * 20 + dr * 20

    def update_motors(self):
        if self.last_angle == self.angle and self.last_speed == self.speed:
            return

        if self.speed == 0 and abs(self.angle) <= 10:
            self.stop_motors()
        elif self.speed == 0:
            angle_speed = self.get_safe_speed(abs(self.angle))
            self.board.motorOn(self.MOTOR_LEFT,  self.DIRECTION_BACKWARD if angle_speed < 0 else self.DIRECTION_FORWARD, angle_speed)
            self.board.motorOn(self.MOTOR_RIGHT, self.DIRECTION_BACKWARD if angle_speed > 0 else self.DIRECTION_FORWARD, angle_speed)
        else:
            direction = self.DIRECTION_FORWARD if abs(self.angle) <= 90 else self.DIRECTION_BACKWARD
            speed_left = self.get_safe_speed(self.speed - (0 if self.angle >= 0 else self.angle))
            speed_right = self.get_safe_speed(self.speed - (0 if self.angle <= 0 else self.angle))
            
            self.board.motorOn(self.MOTOR_LEFT, direction, speed_left)
            self.board.motorOn(self.MOTOR_RIGHT, direction, speed_right)

        self.last_speed = self.speed
        self.last_angle = self.angle
    
    def stop_motors(self):
        self.board.motorOff(self.MOTOR_LEFT)
        self.board.motorOff(self.MOTOR_RIGHT)

    def update(self, stand_still: bool = False):
        if utime.ticks_diff(utime.ticks_ms(), self.last_update_time) > self.sensor_update_interval:
            self.read_sensors()
            self.calculate_movement(stand_still)
            self.update_motors()
            self.last_update_time = utime.ticks_ms()
        
