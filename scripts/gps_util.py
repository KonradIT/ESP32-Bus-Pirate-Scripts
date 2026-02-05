# Parse NMEA packets from a UBlox M10 GPS module hooked up to a Bus Pirate.

from bus_pirate.bus_pirate_wifi import BusPirateWifi
import time
import os
import pynmea2 # pip install pynmea2
from uart_connect_helper import connect_uart
# Connect to the Bus Pirate
bp = BusPirateWifi("192.168.0.57")
bp.start()

connect_uart(bp, 43, 44, 115200, 8, "N", 1, False)

# Start UART read mode
bp.send("read")
bp.wait()
bp.clear_echoes(2)
print("GPS from UART started")

try:
    while True:
        lines = bp.receive(skip=0)
        if lines:
            for line in lines:
                msg = pynmea2.parse(line)
                print(repr(msg))
except KeyboardInterrupt:
    print("\nStopping GPS read...")
finally:
    # Close the connection
    bp.stop()
