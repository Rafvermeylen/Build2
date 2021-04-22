# ---- Imports ----

from machine import UART

# ---- Setup ----

uart = UART(1)

# ---- Code ----
def measurement():
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100,
    pins=('P3', 'P4'))
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes = uart.read(1)

    high = int(uart.read(1)[0])

    low = int(uart.read(1)[0])

    sum = int(uart.read(1)[0])

    distance = (high*256) + low

    if distance < 30:
        print("Hold your horses, buckaroo! That's way too close!")
    else:
        in_cm = distance / 10
        print("Distance: " + str(in_cm) + " cm")
    return distance
