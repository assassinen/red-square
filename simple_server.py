import machine
import time
import socket

pins = [machine.Pin(i, machine.Pin.IN) for i in
        (0, 2, 4, 5, 12, 13, 14, 15)]

def simple_server():

    port = 14900
    # routes = {}
    stop = False
    sock = socket.socket()
    sock.bind(("", port))
    sock.settimeout(2)
    sock.listen(5)

    try:
        while 1:  # работаем постоянно
            try:
                if stop:
                    break
                conn, addr = sock.accept()
                data = '1'
                data = data.encode("utf-8")
                conn.send(data)
                # print("New connection from " + addr[0])
            except:
                continue
            finally:
                # так при любой ошибке
                # сокет закроем корректно
                conn.close()
    finally:
        sock.close()