# Imports
import socket, threading

# Scan a single port
def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        result = sock.connect_ex((ip,port))
        
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed or filtered.")

    except socket.error as e:
        print(f"Error scanning port {port}: {e}")
    
    finally:
        sock.close()

# Scan a range of ports
def scan_ports(ip, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on {ip}...")
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

# Input from user
if __name__ == "__main__":
    target_ip = input("Enter the IP address or hostname to scan: ")
    
    try:
        target_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        print("Invalid IP address or hostname.")
        exit()
    
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    scan_ports(target_ip, start_port, end_port)
