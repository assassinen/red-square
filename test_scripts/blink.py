from machine import Pin
import time
led = Pin(2, Pin.OUT)

def blink(sleep=1):
    while True:
        led.on()
        time.sleep(sleep)
        led.off()
        time.sleep(sleep)