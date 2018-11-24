import machine
import socket
import time

pins_dict = {'GREEN': 12, 'BLUE': 13, 'RED': 15}
pins = dict(zip([k for k in pins_dict.keys()], [machine.Pin(i, machine.Pin.OUT) for i in pins_dict.values()]))

def simple_server():
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>ESP8266 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """

    button_html = """HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nCache-Control: private, no-store\r\n\r\n\
       <!DOCTYPE HTML>\
    <html>\
     <head>\
            <meta charset="UTF-8" />\
            <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> \
            <meta name="viewport" content="width=device-width, initial-scale=1.0"> \
            <title>My control</title>\
       </head><body>\
            <div class="container">\
                <section class="color-1">\
                    <p>\
                        <a href=\"?pin=ON_RED\"><button class="btn btn-4 btn-4a">Red ON</button></a>\
                        <a href=\"?pin=ON_GREEN\"><button class="btn btn-4 btn-4a">Green ON</button></a>\
                    </p>\
                    <p>\
                        <a href=\"?pin=OFF_RED\"><button class="btn btn-5 btn-5a">Red OFF</button></a>\
                        <a href=\"?pin=OFF_GREEN\"><button class="btn btn-5 btn-5a">Green OFF</button></a>\
                    </p>\
                </section>\
            </div>\
    </body></html>"""


    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    status=('ON', 'OFF')

    def all_off():
        for pin in pins.values():
            pin.off()

    def blink(command, color):
        if command == 'ON':
            pins[color].on()
        else:
            pins[color].off()


    def parse_ulr(line):
        # b'Referer: http://192.168.150.7/?pin=OFF1\r\n'
        if 'Referer' in line and '_' in line:
            print(line)
            command, color = str(line).split('=')[1][0:-5].split("_")
            blink(command, color)


    while True:
        cl, addr = s.accept()
        print('client connected from', addr)

        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            parse_ulr(line)
            if not line or line == b'\r\n':
                break

        response = button_html
        cl.send(response)
        cl.close()
