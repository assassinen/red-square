import time
from machine import Pin
led = Pin(2, Pin.OUT)

sleep = 2

def blink():
    led.on()
    time.sleep(sleep)
    led.off()
    time.sleep(sleep)


while True:
    blink()
