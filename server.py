import socket as sk
import random as rn
import time

IP = "192.168.1.4"
port = 12345
sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
sock.bind((IP, port))
print("Server started. Waiting for client requests...\n")
while True:
    data, address = sock.recvfrom(1024)
    print(f"Server received {data.decode()} from {address}")
    random_num = rn.randint(1, 50)
    packet_num = int(data.decode())
    response = str(rn.choice((packet_num, random_num))).encode()
    sock.sendto(response, address)
    print(f"Server sent {response.decode()} to {address}\n")
    time.sleep(1)