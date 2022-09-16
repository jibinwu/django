import pywifi
import sys
import time
from pywifi import const

def gic():
    wifi = pywifi.wifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    if ifaces in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
        print('已连接')
    else:
        print('未连接')
gic()