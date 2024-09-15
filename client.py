import socket as sk
import time

IP = "192.168.1.4"
port = 12345
packet_num = 0
sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
print("Connection with server started\n")
while True:
    sock.sendto(str(packet_num).encode(), (IP, port))
    print(f"Client sent {packet_num} to {IP}:{port}")
    data, address = sock.recvfrom(1024)
    print(f"Client received {data.decode()} from {address}")
    if int(data.decode()) == packet_num:
        packet_num += 1
        print("Packet sent successfully\n")
        time.sleep(1)
    else:
        print("Invalid packet. Requesting again\n")
        time.sleep(1)