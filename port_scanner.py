import socket

def scan_ports(target_host, start_port, end_port):
    open_ports = []

    print(f"Scanning ports on {target_host}...\n")

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target_host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")

            sock.close()

    except socket.error as e:
        print(f"Error: {e}")

    if not open_ports:
        print("No open ports found.")

    return open_ports

if __name__ == "__main__":
    try:
        target_host = input("Enter the target host: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        open_ports = scan_ports(target_host, start_port, end_port)

        print("\nScan complete.")
        if open_ports:
            print("Open ports:", open_ports)
        else:
            print("No open ports found.")

    except ValueError:
        print("Invalid input. Please enter valid port numbers.")
