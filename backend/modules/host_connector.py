import threading
import socket
import random

from .elements.queue import *



class ConnectionsManager:
    def __init__(self):
        self.__connections: dict[tuple[str, int], socket.socket] = {}

    def new(self, clientAddress: tuple[str, int], clientSocket) -> bool:
        if self.__connections[clientAddress] is None:
            self.__connections[clientAddress] = clientSocket
            return True
        else:
            self.__connections[clientAddress].close()
            self.__connections[clientAddress] = clientSocket
            return False

    def get(self, clientAddress: tuple[str, int]) -> socket.socket:
        return self.__connections.get(clientAddress)

    def sendAll(self, data: str) -> None:
        for clientAddress, clientSocket in self.__connections.items():
            clientSocket.send(data.encode())

    def disconnectAll(self) -> None:
        for clientAddress, clientSocket in self.__connections.items():
            clientSocket.close()



class HostConnector:
    __obj = None
    # TCP SOCKET
    __socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __connections = ConnectionsManager()
    __senderQueue: IQueue = StrQueue()


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
            client: socket.socket, clientIp: tuple[str, int] = self.__socket.accept()
            self.__connections.new(clientIp, client)

    def getSenderQueue(self) -> IQueue:
        return self.__senderQueue


    def senderFunction(self):
        while True:
            dataToSend: str = self.__senderQueue.get()

            if dataToSend:
                self.__connections.sendAll(dataToSend)



    def startSender(self) -> None:
        # IN NEW THREAD ONLY!
        threading.Thread(target=self.senderFunction).start()