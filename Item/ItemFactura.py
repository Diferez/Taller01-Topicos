class ItemFactura:
    def __init__(self, iditem, precio, cantidad): #constructor de itemFactura
        self.iditem = iditem
        self.precio = precio 
        self.cantidad = cantidad

    def getItemFactura(self): #retorna el itemFactura
        return self.iditem, self.precio


