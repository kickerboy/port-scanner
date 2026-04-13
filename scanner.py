import socket

target = input("Enter target: ")
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning {target}...\n")

for port in range(start, end + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()
