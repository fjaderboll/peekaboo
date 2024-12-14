from time import sleep

from ultrasonic import Ultrasonic

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
