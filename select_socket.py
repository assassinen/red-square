import socket, select
from machine import Pin
led = Pin(2, Pin.OUT)
sleep = 1


def handle_pin(conn, client_addr):
    data = conn.recv(1024).decode("utf-8").strip("\r\n")
    try:
        if data == '1':
            led.off()
        elif data == '0':
            led.on()
        else:
            conn.send("Bad params: %s \r\n" % str(data))
    except:
        conn.send("Bad params: %s \r\n" % str(data))
    conn.close()


def serv(port=14900):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (socket.getaddrinfo("0.0.0.0", port))[0][-1]
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(4)

    while True:
        r, w, err = select.select((sock,), (), (), 1)
        if r:
            for readable in r:
                conn, conn_addr = sock.accept()
                handle_pin(conn, conn_addr)
    # a cюда можно вставить обработку еще-чего-то
    # а можно вставить такую обработку по таймеру

serv()