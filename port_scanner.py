#comment
import socket
from colorama import Fore

GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET


def portScanner(host, port):
    # create socket object
    sock = socket.socket()
    try:
        sock.connect((host, port))
        sock.settimeout(0.2)
    except:
        return False
    else:
        return True





def runner():
    host = input("Please enter the host to scan: ")
    count = 0
    for port in range(1, 1000):
        if (portScanner(host, port)):
            print(f"{GREEN}[+]The port {port} is open on {host}! {RESET}")
        else:
            count = count + 1

            print(f"{GRAY}[-] {count} Ports are closed!{RESET}", end="\r")

if __name__ == "__main__":
    runner()
