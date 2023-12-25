import struct


class ICMP:

    # unpacks the ICMP Packets (segments)
    def __init__(self,data):

        self.icmp_type, self.code, self.checksum = struct.unpack("! B B H", data[:4])
        self.payload = data[4:]
