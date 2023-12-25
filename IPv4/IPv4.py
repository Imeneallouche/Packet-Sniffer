import struct
from Utilities.general import get_ipv4


HEADER_INFORMATION_LENGTH = 20

# unpack the ipv4 packet

class IPv4:

    def __init__(self, data):

        # version & header_length are 2 infos mixed in 1 byte = 8 bits ********
        version_header_length = data[0]

        # Extract the version : first 4 bits   ****____
        self.version = version_header_length >> 4

        # Extract the header length : last 4 bits   ****____
        self.header_length = (version_header_length & 15) * 4

        self.ttl, self.ip_protocol, dest_ip, src_ip = struct.unpack("! 8x B B 2X 4s 4s", data[:HEADER_INFORMATION_LENGTH])

        # turn the binary ip addresses into human readbale ones
        self.dest_ip = get_ipv4(dest_ip)
        self.src_ip = get_ipv4(src_ip)

        # the payload where the data is 
        self.payload = data[int(self.header_length):]