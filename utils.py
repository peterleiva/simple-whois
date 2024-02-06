import socket
import sys

def find_ip(target):
    try:
        ip_addr = socket.gethostbyname(target)
        return ip_addr
    except socket.gaierror as e:
        print(f"Error: {e}")
        sys.exit(2)
