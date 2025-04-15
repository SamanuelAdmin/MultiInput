import threading
import socket


class Connector:
    __obj = None
    # TCP SOCKET
    __socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super(Connector, cls).__new__(cls)

        return cls.__obj

    def __init__(self, ip: str, port: int):
        self.__socket.connect((ip, port))

    def listenEvents(self):
        pass