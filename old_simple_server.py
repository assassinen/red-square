
import machine
import socket

pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15, 16)]

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
                        <a href=\"?pin=ON1\"><button class="btn btn-4 btn-4a">Back ON</button></a>\
                        <a href=\"?pin=ON2\"><button class="btn btn-4 btn-4a">Bra ON</button></a>\
                    </p>\
                    <p>\
                        <a href=\"?pin=OFF1\"><button class="btn btn-5 btn-5a">Back OFF</button></a>\
                        <a href=\"?pin=OFF2\"><button class="btn btn-5 btn-5a">Bra OFF</button></a>\
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

    def get_url(conn):
        conn_file = conn.makefile('rb', 0)
        method, url = None, None
        while True:
            line = conn_file.readline().decode()
            if not line or line == '\r\n':
                break
            if line.startswith('GET'):
                method, url, _ = line.split()
        return method, url

    def parse_url(url):
        try:
            path, query = url.split('?', 2)
        except:
            return url, {}
        return path, {_.split('=')[0]: _.split('=')[1] for _ in
                      query.split('&')}

    def parse_ulr(line):
        print(line)
        pass

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

        # conn, addr = s.accept()
        # method, url = get_url(conn)
        # path, query = parse_url(url)
        # print(addr[0], '-', method, url)
        # if path == '/':
        #     if [_ for _ in list('rbg') if _ in query.keys()]:
        #         led.set(query.get('r', 0), query.get('g', 0),
        #                 query.get('b', 0))
        #     rows = [
        #         '<tr><td>%s</td><td>%s</td></tr>' % (str(p), status[p.value()])
        #         for p in pins]
        #     response = html % '\n'.join(rows)
        #     # response = template.py % (led.r, led.g, led.b)
        #     conn_send(conn, response)
        # conn.close()