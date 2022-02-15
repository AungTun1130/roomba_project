import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 3000
s.bind((IP, PORT))
s.listen()
print("Server listening @ {}:{}".format(IP, PORT))
conn, addr = s.accept()
while True:
    #print("Listening...")
    #print("Got connection from", addr)
    msg = conn.recv(1024)
    conn.send(bytes("Thank you", "utf-8"))
    # print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
    # send_data = input("Type some text to send => ")
    # s.sendto(send_data.encode('utf-8'), addr)
    # print("\n\n 1. Server sent : ", send_data, "\n\n")

    print(msg)
    time.sleep(1)
conn.close()