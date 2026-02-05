from bus_pirate.bus_pirate import BusPirate
from bus_pirate.bus_pirate_wifi import BusPirateWifi

# Small helper to connect to a UART port on the Bus Pirate.
def connect_uart(bp: BusPirate | BusPirateWifi, rx_pin: int, tx_pin: int,
    baudrate: int = 115200, bits = 8, parity = "N", stop = 1, inverted: bool = False):
    bp.send("mode uart")
    received = bp.receive()
    if "Mode changed to UART" in received:
        bp.send("config")
    bp.send(f"{rx_pin}\n")
    bp.send(f"{tx_pin}\n")
    bp.send(f"{baudrate}\n")
    bp.send(f"{bits}\n")
    bp.send(f"{parity}\n")
    bp.send(f"{stop}\n")
    if inverted:
        bp.send("y\n")
    else:
        bp.send("n\n")
        
    bp.wait()
    bp.clear_echoes(2)
    print(bp.receive())

if __name__ == "__main__":
    # Connect to the Bus Pirate
    bp = BusPirateWifi("192.168.0.57")
    bp.start()
    connect_uart(bp, 44, 43, 115200, 8, "N", 1, False)