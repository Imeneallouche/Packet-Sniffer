import struct
import socket
from Utilities.general import get_mac_address



MAC_ADDR_SIZE = 6
PROTOCOL_TYPE_SIZE = 2
TAB_1 = '  '



class Ethernet:
    def __init__(self, data):
        # Unpack the Ethernet frame
        DESTINATION_MAC, SOURCE_MAC, PROTOCOL_TYPE = struct.unpack(f"! {MAC_ADDR_SIZE}s {MAC_ADDR_SIZE}s H", data[:MAC_ADDR_SIZE*2 + PROTOCOL_TYPE_SIZE])

        # Convert the binary MAC addresses to readable format
        self.dest_mac = get_mac_address(DESTINATION_MAC)
        self.src_mac = get_mac_address(SOURCE_MAC)

        # Convert the protocol type to a human-readable format
        self.protocol = socket.htons(PROTOCOL_TYPE)

        # Extract the pure data from the Ethernet frame
        self.data = data[MAC_ADDR_SIZE*2 + PROTOCOL_TYPE_SIZE:]



    def print_ethernet_frame(self):
        print('\nEthernet Frame:')
        print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(self.dest_mac, self.src_mac, self.protocol))
        print("\n\n\n ____________Ethernet Frame____________ ")
        print(f"\n Source Mac Address: {self.src_mac}")
        print(f"\n Destination Mac Address: {self.dest_mac}")
        print(f"\n Ethernet protocol: {self.protocol}")
        print("\n ______________________________________ ")

    