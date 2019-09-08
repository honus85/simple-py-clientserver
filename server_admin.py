from subscriber import Subscriber
from publisher import Publisher
import threading

port = 63000
host = '127.0.0.1'


def start_subscriber():
    subscriber = Subscriber(host, port)
    subscriber.listen()


def start_server():
    x = threading.Thread(target=start_subscriber, args=())
    x.start()


def stop_server():
    publisher = Publisher(host, port)
    publisher.publish_disconnect()
