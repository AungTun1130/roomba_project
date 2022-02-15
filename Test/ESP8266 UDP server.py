import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Listening...")
s.sendto("hi".encode(), ('192.168.0.104', 4210))
while True:

    data, address = s.recvfrom(4096)
    print("\n 2. Client received: ", data.decode('utf-8'), "\n")
    send_data = input("Type some text to send => ")
    s.sendto(send_data.encode('utf-8'), address)
    print("\n 1. Server sent : ", send_data, "\n")
    time.sleep(1)