import utils
import socket
import re

WHOIS_PORT = 43
IANA_WHOIS_SERVER = "whois.iana.org"

def _get_refer_server(res):
    try:
        founded = re.findall(r'refer:\s*(.+)\n', res)[0]
        return founded
    except IndexError:
        return None

def query(target, server = IANA_WHOIS_SERVER, port = WHOIS_PORT):
    whois_ip_addr = utils.find_ip(server)
    print(f"found IP {whois_ip_addr}")

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((whois_ip_addr, port))

    conn.send(f"{target}\r\n".encode())

    res = conn.recv(4 * 2**10).decode()
    conn.close()

    # while _get_refer_server(res) is not None:
    #     print("refer at", _get_refer_server(res))
    #     res += query(target, server=_get_refer_server(res))

    return res
