import time
from machine import Pin
led = Pin(2, Pin.OUT)

sleep = 1

def blink():
    led.off()
    time.sleep(sleep)
    led.on()
    time.sleep(sleep)

