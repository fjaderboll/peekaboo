import time
from machine import Pin, Timer

ledPin = Pin("LED", Pin.OUT)
ledTimer = Timer(period=500, mode=Timer.PERIODIC, callback=lambda t: ledPin.toggle())
#ledTimer.init(period=500, mode=Timer.PERIODIC, callback=lambda t: ledPin.toggle())

time.sleep(60)
