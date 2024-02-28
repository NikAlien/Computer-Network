import socket

DISCONNECT_MSG = "!QUIT"
FORMAT = 'utf-8'
HEADER = 64
PORT = 7777
SERVER = "172.30.111.175"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def run():
    print(client.recv(19).decode(FORMAT))
    for i in range(7):
        print(client.recv(100).decode(FORMAT))
        msg = input("--> ")
        client.send(msg.encode(FORMAT))
    print(client.recv(47).decode(FORMAT))
    print(client.recv(23).decode(FORMAT))

run()