from network import LoRa
import time
import ubinascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

dev_eui = ubinascii.unhexlify('00845EA96B3F91BB')
app_eui = ubinascii.unhexlify('70B3D57ED003E4C7')
app_key = ubinascii.unhexlify('6B5F52E209E79779B83FF235EF6A6DF6')

def findLora():
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

    while not lora.has_joined():
        print("Not yet joined...")
        time.sleep(2.5)

    print("Joined")
    return lora
