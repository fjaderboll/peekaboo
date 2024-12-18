from machine import Pin
import time

def handle_pir_rising(pin):
	print("PIR rising:", pin.value())

def handle_pir_falling(pin):
	print("PIR falling:", pin.value())

pirPin = Pin(19, Pin.IN)
print('hello')
print("PIR initial value:", pirPin.value())
pirPin.irq(trigger=Pin.IRQ_RISING, handler=handle_pir_rising)
pirPin.irq(trigger=Pin.IRQ_FALLING, handler=handle_pir_falling)

time.sleep(60)
