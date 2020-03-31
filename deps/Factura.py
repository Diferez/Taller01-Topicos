import time
class Factura:
    #Constructor de Factura
    def __init__(self, nroFactura, estado, cliente):
        self.nroFactura = nroFactura
        self.fechaFactura = time.strftime("%H:%M:%S")
        self.estado = estado
        self.items = []
        self.cliente = cliente
        self.totalFactura = None

    #getter del total
    def getTotal(self):
        return self.getTotal

    #Suma de los items
    def sumaTotal(self):
        total = 0
        for x in self.items:
            total += x.precio
        self.totalFactura = total
        
    #getter del estado (pagado o no pagado)
    def getEstado(self):
        return self.estado

    #setter del estado (pagado o no pagado)
    def setEstado(self, estado):
        self.estado = estado

    #getter del numero de factura
    def getNro(self):
        return self.nroFactura
    
    #getter de la fecha en la que se realiza la factura
    def getFecha(self):
        return self.fechaFactura

    #Getter del cliente
    def getCliente(self):
        return self.cliente

    #Getter del item
    def getItems(self):
        return self.items

    #añadir nuevo item a la factura
    def addItems(self, item):
        self.items.append(item)

    #eliminar un item de la factura
    def eliminarItems(self, item):
        self.items.remove(item)

    def toString(self):
        stri = str("Id " + str(self.nroFactura) + "\n" +
            "Fecha Factura " + self.fechaFactura + "\n" +
            "Estado " + self.estado + "\n" +
            "Cliente " + self.cliente + "\n" +
            "Total " + str(self.totalFactura) + "\n")
        for i in self.items:
            stri += str(i.iditem)+" "+str(i.precio)+"\n"
        
        stri += "+=+=+=+=+=+=+=+=+=+=+=+=+=+="

        return stri


        
        