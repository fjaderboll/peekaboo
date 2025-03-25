from machine import Pin
import time

def show_pir_value(name, value):
	print(f'PIR {name}: {value} (elapsed time: {time.ticks_diff(time.ticks_ms(), startTime)/1000:.1f} s)')
	ledPin.value(value)

def pir_irq(pin):
	show_pir_value('irq', pin.value())

pirPin = Pin(19, Pin.IN)
ledPin = Pin("LED", Pin.OUT)
startTime = time.ticks_ms()

show_pir_value('initial', pirPin.value())
pirPin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=pir_irq)

time.sleep(120)
show_pir_value('end', pirPin.value())
