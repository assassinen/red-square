from esp8266_network import set_network
from blink_server import simple_server

if __name__ == "__main__":
    set_network()
    simple_server()
