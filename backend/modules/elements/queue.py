from abc import ABC, abstractmethod



class IQueue(ABC):
    def __init__(self): ...
    def add(self, obj: object) -> None: ...
    def get(self) -> object: ...
    def isEmpty(self) -> bool: ...


class Queue:
    def __init__(self):
        self.__elements: list = []

    def add(self, obj: object) -> None:
        self.__elements.append(obj)

    def get(self) -> object:
        self.__elements.pop(0)

    def isEmpty(self) -> bool:
        return len(self.__elements) == 0