from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def getItem(self):
        raise NotImplementedError

    @abstractmethod
    def getValor(self):
        raise NotImplementedError