from machine import Pin
import time
led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep(3)
    led.off()
    time.sleep(3)