from esp8266_network import set_network, set_host_point
from simple_server import simple_server
from rgb_lamp import rgb_lamp
# from blink import blink
import time
from machine import Pin
led = Pin(2, Pin.OUT)
sleep = 1

if __name__ == "__main__":
    set_host_point()
    set_network()
    time.sleep(sleep)
    led.off()
    print('on')
    time.sleep(sleep)
    led.on()
    simple_server()
