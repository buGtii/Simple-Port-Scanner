import socket
import threading
from colorama import Fore, Style

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(Fore.GREEN + f"[+] Port {port} is OPEN --> {banner}")
        else:
            print(Fore.RED + f"[-] Port {port} is CLOSED")
        sock.close()
    except:
        pass

def main():
    print(Fore.CYAN + "=== Simple Port Scanner ===" + Style.RESET_ALL)
    target = input("Enter target (IP or hostname): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    try:
        host = socket.gethostbyname(target)
        print(Fore.YELLOW + f"Scanning host: {host}" + Style.RESET_ALL)
    except socket.gaierror:
        print(Fore.RED + "Host not found!" + Style.RESET_ALL)
        return

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
