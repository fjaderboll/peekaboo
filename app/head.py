from machine import SoftI2C
import utime

from PicoRobotics import KitronikPicoRobotics
from amg88xx import AMG88XX

class Head:
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'

    YAW_MIN = 30
    YAW_MIDDLE = 90
    YAW_MAX = 150
    PITCH_MIN = 60
    PITCH_MIDDLE = 90
    PITCH_MAX = 110

    def __init__(self, board: KitronikPicoRobotics, i2c0: SoftI2C, servo_yaw: int, servo_pitch: int):
        self.board = board
        self.servo_yaw = servo_yaw
        self.servo_pitch = servo_pitch
        self.yaw = 0
        self.pitch = 0
        self.first_update = True
        self.first_print = True
        self.heat = AMG88XX(i2c0)
        self.update_interval = 50
        self.last_update_time = 0
        self.step_size = 5
        self.found_someone = False
    
    def get_yaw(self):
        return self.yaw

    def get_direction_angle(self):
        return (self.yaw - self.YAW_MIDDLE) * -1

    def get_pitch(self):
        return self.pitch

    def find_low_high(self):
        low = 100
        high = 0
        for row in range(8):
            for col in range(8):
                temp = self.heat[row, col]
                if temp < low:
                    low = temp
                if temp > high:
                    high = temp
        
        if low == high:
            high += 1
        
        return (low, high)

    def normalize(self, low, high):
        norm = [[0 for i in range(8)] for j in range(8)]
        for row in range(8):
            for col in range(8):
                norm[row][col] = (self.heat[row, col] - low)/(high - low)
        
        return norm

    def find_weight_center(self, arr):
        wx = 0
        wy = 0
        s = 0
        for x in range(8):
            for y in range(8):
                v = arr[x][y]
                if v > 0.9:
                    wx += v * x
                    wy += v * y
                    s  += v
        
        if s == 0:
            return (0, 0)
        
        (rx, ry) = ((wx / s - 4) / 4, (wy / s - 4) / 4)
        return (-ry, rx)  # consider sensor rotation

    def render_pixel(self, v):
        chars = ' .:oO@'
        i = int(v*10/2)
        return chars[i]

    def update_head_position(self, new_yaw=0, new_pitch=0):
        new_yaw = int(new_yaw)
        new_pitch = int(new_pitch)

        if new_yaw != self.yaw:
            self.yaw = new_yaw
            self.board.servoWrite(self.servo_yaw, self.yaw)
        if new_pitch != self.pitch:
            self.pitch = new_pitch
            self.board.servoWrite(self.servo_pitch, self.pitch)

    def move_head(self, wx, wy):
        new_yaw = max(self.YAW_MIN, min(self.YAW_MAX, self.yaw + wx * self.step_size))
        new_pitch = max(self.PITCH_MIN, min(self.PITCH_MAX, self.pitch + wy * self.step_size))
        self.update_head_position(new_yaw, new_pitch)
    
    def print_state(self, print_camera=True, use_numbers=False):
        if print_camera:
            if self.first_print:
                self.first_print = False
            else:
                for row in range(8+1):
                    print(self.LINE_UP, end=self.LINE_CLEAR)
            
            for row in range(8):
                for col in range(7, -1, -1):
                    if use_numbers:
                        temp = self.heat[row, col]
                        print(' {:3d}'.format(temp), end='')
                    else:
                        v = self.temp_norm[row][col]
                        s = self.render_pixel(v)
                        print(s, end=' ')
                print()
        
        print(f'wx: {self.wx:.1f} wy: {self.wy:.1f} found_someone: {self.found_someone}')
    
    def has_found_someone(self):
        return self.found_someone
    
    def sleep_position(self, instant=False):
        if not instant:
            steps = 10
            yaw_step = (self.YAW_MIDDLE - self.yaw) // steps
            pitch_step = (self.PITCH_MAX - self.pitch) // steps
            for _ in range(0, steps):
                self.update_head_position(self.yaw + yaw_step, self.pitch + pitch_step)
                utime.sleep_ms(30)
        self.update_head_position(self.YAW_MIDDLE, self.PITCH_MAX)

    def update(self):
        if utime.ticks_diff(utime.ticks_ms(), self.last_update_time) > self.update_interval:
            # update data
            self.heat.refresh()
            (low, high) = self.find_low_high()
            self.temp_norm = self.normalize(low, high)
            (self.wx, self.wy) = self.find_weight_center(self.temp_norm)

            # detect human
            th = 0.5
            averageTemp = 0
            if -th <= self.wx <= th and -th <= self.wy <= th:
                for row in range(2, 6):
                    for col in range(2, 6):
                        temp = self.heat[row, col]
                        averageTemp += temp / 16
            self.found_someone = (averageTemp > 25)

            # move head
            if self.first_update:
                self.update_head_position(self.YAW_MIDDLE, self.PITCH_MIDDLE)
                self.first_update = False
            else:
                self.move_head(self.wx, self.wy)
            
            self.last_update_time = utime.ticks_ms()
            return True
        return False
