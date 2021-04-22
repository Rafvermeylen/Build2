import pycom
from network import WLAN
import machine
import time

# ---- Setup ----

wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

# ---- Loop ----
def searchWifi(yourSSID, yourPassword):
    while not wlan.isconnected():
        #In school WPA2 ipv WPA
        wlan.connect(ssid=yourSSID, auth=(WLAN.WPA, yourPassword))
        time.sleep(2)
        pycom.rgbled(0xFF0000)          # Red
        print("no connection")
    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)              # Green
