import socket
import threading

class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    def bind(self, IP_and_PORT: tuple):
        self.socket.bind(IP_and_PORT)
    def listen(self):
        self.socket.listen()
    def accept_and_recv(self):
        while True:
            self.client_connection_socket, (client_ip, port) = self.socket.accept()
            data = ""
            while True:
                data = ""
                while "\n" not in data:   
                    data += self.client_connection_socket.recv(4096).decode("utf-8")
                print(f"{client_ip}:", data)

    def close_connection(self):
        self.client_connection_socket.close()


class Client():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect_to(self, target: tuple):
        self.socket.connect(target)
    def recv_message(self):
        data = ""
        while True:
            chunk = self.socket.recv(1024).decode("utf-8")
            if chunk == "":
                break
            data += chunk
            while "\n" in data:
                message, data = data.split("\n",1)
                print(message)

    def message(self, data: str):
        self.socket.sendall(f"{data}\n".encode(encoding="utf-8"))



server1 = Server()
client1 = Client()

thread1 = threading.Thread(target=server1.accept_and_recv)

server1.bind(("127.0.0.1", 9000))
server1.listen()
client1.connect_to(("127.0.0.1",9000))

thread1.start()#accept_recv server

text = ""
while text != "close":
    text = input()
    client1.message(text)
client1.socket.close()
