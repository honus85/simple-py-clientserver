import json
import socket


class Publisher(object):

    def __init__(self, host, port=1337):
        self.host = host
        self.port = port
        self._timeout = None
        self._address = host

    def publish(self, order):
        order_dict = json.dumps(order.__dict__)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        with self.socket as s:
            s.send(order_dict.encode())
            data = s.recv(1024)
            while data.decode() != 'Ack':
                print("waiting ack...")
            print('Received from server ', repr(data))

    def close(self):
        self.socket.close()

    def publish_disconnect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        with self.socket as s:
            s.send("Disconnect".encode())



