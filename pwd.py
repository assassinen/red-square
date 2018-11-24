
from machine import Pin, PWM
import time, math

led = Pin(2, Pin.OUT)
# red = PWM(Pin(15), freq=1000)
# green = PWM(Pin(12), freq=1000)
# blue = PWM(Pin(13), freq=1000)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

if __name__ == "__main__":
    # set_network()
    # simple_server()

    # led = Pin(2, Pin.OUT)
    # led.on()
    # led.off()

    red = PWM(Pin(15), freq=1000)
    green = PWM(Pin(12), freq=1000)
    blue = PWM(Pin(13), freq=1000)

    for i in range(30):
        pulse(red, 20)
        pulse(green, 20)
        pulse(blue, 20)
