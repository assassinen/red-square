import machine
import time


pins_dict = {'GREEN': 12, 'BLUE': 13, 'RED': 15}

pins = dict(zip([k for k in pins_dict.keys()], [machine.Pin(i, machine.Pin.OUT) for i in pins_dict.values()]))

def all_off():
    for pin in pins.values():
        pin.off()

def blink(colors, sleep):
    singl_colols = []
    for color in colors:
        if color == 'WHAIT':
            singl_colols = ['GREEN', 'RED', 'BLUE']
        elif color == 'YELLOW':
            singl_colols = ['GREEN', 'RED']
        else:
            singl_colols.append(color)

        for color in singl_colols:
            pins[color].on()
        time.sleep(sleep)
        all_off()
        singl_colols.clear()
        time.sleep(sleep)


if __name__ == "__main__":
    colors = ['YELLOW', 'GREEN', 'BLUE', 'WHAIT']
    while True:
        blink(colors, 1)