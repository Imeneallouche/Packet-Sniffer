import textwrap

# Convert binary MAC address to a readable format (e.g., "00:11:22:33:44:55")
def get_mac_address(mac_binary):

    # Convert each byte in the binary MAC address to a hexadecimal string
    # each pair of characters is zero-padded and in uppercase.
    mac_addr = ':'.join(f'{x:02X}' for x in mac_binary)

    return mac_addr




# Convert binary IP address to a readable format (e.g., "127.0.0.1")
def get_ipv4(ip_binary):

    # Unpack the binary IP address using socket.inet_ntoa
    #ip_addr = socket.inet_ntoa(ip_binary)

    #OR
    ip_addr = '.'.join(map(str, ip_binary))

    return ip_addr


# Formats multi-line data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])
