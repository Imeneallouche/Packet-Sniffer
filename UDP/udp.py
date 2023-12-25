import struct


class UDP:
    # unpacks UDP packets (segments)
    def __init__(self,data):
        self.src_port, self.dest_port, self.size = struct.unpack("! H H 2X H", data[:8])
        self.payload = data[8:]






