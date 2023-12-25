import struct


class TCP:

    # unpacks TCP packets (segments)
    def __init__(self,data):

        self.src_port, self.dest_port, self.sequence, self.ackowledgement, offset_reserved_flags = struct.unpack("! H H L L H", data[:14])
        
        OFFSET = (offset_reserved_flags >> 12) *4

        self.payload = data[OFFSET:]

        self.flag_urg = (offset_reserved_flags & 32) >> 5    #   the urg flag
        self.flag_ack = (offset_reserved_flags & 16) >> 4    #   the Acknowledgment flag
        self.flag_psh = (offset_reserved_flags & 8) >> 3     #   the push flag
        self.flag_rst = (offset_reserved_flags & 4) >> 2     #   the reset flag
        self.flag_syn = (offset_reserved_flags & 2) >> 1     #   the push flag
        self.flag_fin = (offset_reserved_flags & 1)          #   the finish flag
