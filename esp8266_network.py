import network

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

def get_info_network(network_type=None):
    if network_type == 'STA':
        # 192.168.150.6
        return sta_if.ifconfig()
    else:
        return ap_if.ifconfig()

def get_ip(network_info=None):
    return get_info_network(network_info)[0]

def set_network():
    sta_if.active(True)
    sta_if.connect('122P-330W', 'zyxel-684-ias')
    sta_if.ifconfig()

def set_host_point():
    ap_if.active(True)
    ap_if.config(essid='RSExecutor')
    ap_if.config(password='RSExecutor')


if __name__ == "__main__":
    get_ip()
