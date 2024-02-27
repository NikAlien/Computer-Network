import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 7777
SERVER = "172.30.111.175"
ADDR = (SERVER, PORT)
correct_ans = ["D", "C", "A", "A", "B", "C", "D"]
questions = ["\nWhat is 1 + 1? \nA) 2\nB) 10\nC) 3 - 1\nD) All of the above\n",
             "\nHow many legs does a spider have? \nA) 6\nB) 12\nC) 8\nD) 10\n",
             "\nWhere does Santa Claus live? \nA) The North Pole\nB) The South Pole\nC) Hawaii\nD) Hollywood\n",
             "\nWhat is a group of lions called? \nA) Pride\nB) Bank\nC) School\nD) Rich\n",
             "\nHow many continents are there? \nA) 6\nB) 7\nC) 8\nD) 6.5\n",
             "\nWhat is the closest star to Earth? \nA) Sirius\nB) Alpha Centauri\nC) Helios\nD) Tau Ceti\n",
             "\nHow many bones does a shark have? \nA) 206\nB) 150\nC) 35\nD) 0\n"]
# in case we don't look for the IP address
# SERVER = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("WELCOME TO THE QUIZ".encode(FORMAT))
    ans = []

    for i in range(7):
        conn.send(questions[i].encode(FORMAT))
        msg = conn.recv(10).decode(FORMAT)
        UP = msg.upper()
        print(f"[{addr}] {UP}")
        ans.append(UP)

    count = 0
    for i in range(7):
        if correct_ans[i] == ans[i]:
            count += 1
    msg = f"You have {count} correct answers and {7 - count} wrong ones :)\n"
    conn.send(msg.encode(FORMAT))
    conn.send("-- HOPE YOU HAD FUN --".encode(FORMAT))

    conn.close()
    print(f"[LOSS OF CONNECTION] {addr} disconnected.")


def start():
    s.listen()
    print(f"[LISTENING MODE] Server is listening on {SERVER}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\n[ACTIVE CONNECTIONS] Currently active: {threading.active_count() - 1} threads")

print("[STARTING] server is starting...")
start()