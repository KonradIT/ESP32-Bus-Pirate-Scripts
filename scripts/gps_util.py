# Parse NMEA packets from a UBlox M10 GPS module hooked up to a Bus Pirate.

from bus_pirate.bus_pirate_wifi import BusPirateWifi
import time
import os
import pynmea2 # pip install pynmea2

# Connect to the Bus Pirate
bp = BusPirateWifi("192.168.0.57")
bp.start()

# Change to UART mode
bp.change_mode("uart")

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
