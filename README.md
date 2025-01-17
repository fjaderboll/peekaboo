# Peek-a-boo
**NOTE** *Very early in development, it does currently not work as intended*

A mobile robot that like to play hide-n-seek with you or just
follow you around.

![prototypes](doc/prototypes-collage.jpg "Prototypes")

More technically, it will use a heat camera to detect humans
and ultrasonic sensors for navigating a flat surface with obstacles.
If left unattended it will go to asleep and awoken by a PIR sensor.

## Parts
* Microcontroller: [Raspberry Pi Pico H](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family) ([pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg))
* ~~Display: SH1107 ([library](https://github.com/peter-l5/SH1107))~~
* Heat camera: AMG8833 ([library](https://github.com/peterhinch/micropython-amg88xx))
* Motor/servo shield: [Kitronik Robotics Board](https://github.com/KitronikLtd/Kitronik-Pico-Robotics-Board-MicroPython) ([pinout](https://kitronik.co.uk/cdn/shop/products/5329_additional-1-kitronik-robotics-board-for-raspberry-pi-pico_800x.jpg))
* Servo motors: 2 x SG90
* Movement detection: PIR
* Ultrasonic sensors: 4 x HC-SR04
* Sound: Passive piezo buzzer
* Case/structure: [3D printed parts](case/README.md)

## IDE
Either works:
* Visual Studio Code - extension `MicroPico`
* Thonny: `pip3 install thonny -U`

## Deploy software
Upload content in folder `app` into root of the microcontroller. (VSCode command `MicroPico: Upload project to Pico`)
