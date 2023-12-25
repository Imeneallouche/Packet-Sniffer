import struct
import time

class Pcap:

    def __init__(self, filename, link_type=1):
        
        """
        Initializes a Pcap object.

        :param filename: The name of the pcap file.
        :param link_type: The link layer type (default is 1 for Ethernet).
        """

        self.pcap_file = open(filename, 'wb')
        
        # Pcap file header format: magic_number, version_major, version_minor, thiszone, sigfigs, snaplen, link_type
        self.pcap_file.write(struct.pack('@ I H H i I I I', 0xa1b2c3d4, 2, 4, 0, 0, 65535, link_type))

    def write(self, data):
        """
        Writes a packet to the pcap file.

        :param data: The packet data to be written.
        """
        ts_sec, ts_usec = map(int, str(time.time()).split('.'))
        length = len(data)
        # Pcap record header format: ts_sec, ts_usec, incl_len, orig_len
        self.pcap_file.write(struct.pack('@ I I I I', ts_sec, ts_usec, length, length))
        self.pcap_file.write(data)

    def close(self):
        """Closes the pcap file."""
        self.pcap_file.close()


# Example Usage:
# pcap_instance = Pcap("example.pcap", link_type=1)
# pcap_instance.write(b'\x00\x01\x02\x03')  # Replace this line with your actual packet data
# pcap_instance.close()
