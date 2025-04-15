import threading
import socket
import random

from .elements.queue import *


class HostConnector:
    __obj = None
    # TCP SOCKET
    __socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __connections = []
    __senderQueue: IQueue = Queue()


    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super(HostConnector, cls).__new__(cls)

        return cls.__obj

    def __init__(self, ip: str, port: int):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((ip, port))
        self.__socket.listen()
        threading.Thread().start()


    def clientCatcher(self):
        while True:
            client: socket.socket, clientIp: set[str, int] = self.__socket.accept()


    def senderFunction(self):
        while True:
            if not self.__senderQueue.isEmpty():



    def startSender(self) -> None:
        # IN NEW THREAD!
        threading.Thread(target=self.senderFunction).start()