import socket


class Subscriber(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self):
        with self.socket as s:
            s.bind((self.host, self.port))
            s.listen(5)
            while True:
                conn, peer_port = s.accept()
                with conn:
                    print('Connected by ', peer_port)
                    data = conn.recv(1024)
                    print(data.decode())
                    if data.decode() == 'Disconnect':
                        print("Disconnect Received")
                        conn.close()
                        break
                    conn.send("Ack".encode())
