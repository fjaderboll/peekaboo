from machine import Pin, I2C

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400_000)
devs = i2c.scan()
print(f"Found {len(devs)} devices")
for dev in devs:
    print('i2c device found:', dev)
