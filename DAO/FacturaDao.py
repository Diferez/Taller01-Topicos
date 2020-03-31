from abc import ABC, abstractmethod

class FacturaDao(ABC):
    @abstractmethod
    def crearFactura(self):
        raise NotImplementedError
    @abstractmethod
    def actualizarFactura(self):
        raise NotImplementedError
    @abstractmethod
    def eliminarFactura(self):
        raise NotImplementedError
    @abstractmethod
    def verFacturas(self):
        raise NotImplementedError