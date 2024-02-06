import utils
import socket

WHOIS_PORT = 43
IANA_WHOIS_SERVER = "whois.iana.org"

def _get_refer_server(res):
    try:
        urls = filter(lambda x: x.startswith("refer") or x.startswith("whois"), res.split("\n"))
        return list(map(lambda x: x.split(":")[1].strip(), urls))[0]
    except IndexError:
        return None

def query(target, server = IANA_WHOIS_SERVER, port = WHOIS_PORT):
    whois_ip_addr = utils.find_ip(server)

    conn = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    conn.connect((whois_ip_addr, port))

    conn.send(f"{target}\r\n".encode())

    res = ''

    while True:
        data = conn.recv(4 * 2**10)
        if not data:
            break
        res += data.decode('utf-8', 'ignore')

    conn.close()

    refer = _get_refer_server(res)

    if not refer:
        return res
    
    res += f"# {refer} \n\n"

    return res + query(target, refer, port)
