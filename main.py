import wifi
import connectToWifi
import time

#connected = False

#In school WPA2 ipv WPA
connectToWifi.searchWifi('Ronny', '0477279195')

while True:
    #wifi.sendLora(connected)
    #connected = True
    wifi.sendWifi()
    time.sleep(5)
