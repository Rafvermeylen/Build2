# ---- Imports ----
import connectToWifi
import connectToLora
import request
import ultrasonic
import ustruct
import socket
import time


def sendLora(connected):
    if not connected:
        lora = connectToLora.findLora()
        packet = ustruct.pack('f', ultrasonic.measurement())
    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
    # send some data
    s.send(bytes([0x01, 0x02, 0x03]))
    s.send(packet)
    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)


def sendWifi():

    aio_key = "aio_oGTN07bf50gNGqLaGXmLFPkZY9nT"
    username = "rafvermeylen"
    feed_name = "Ultrasonic"

    ultra = ultrasonic.measurement()
    url = 'https://io.adafruit.com/api/v2/rafvermeylen/feeds/ultrasonic/data'
    body = {'value': ultra}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = request.post(url, json=body, headers=headers)
        print(r.text)
    except Exception as e:
        print(e)
    time.sleep(5)
