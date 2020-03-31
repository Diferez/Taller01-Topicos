from Item.Item import Item

class ItemPesoImpl(Item):
    def __init__(self, tipoItem, id, descripcion, valorUnidad):
        self.tipoItem = tipoItem
        self.id = id
        self.descripcion = descripcion
        self.valorUnidad = valorUnidad
    
    def calcTotal(self, quant):
        return (quant/1000)*self.valorUnidad
    def getItem(self):
        return self.id
    
    def getValor(self):
        return self.valorUnidad

    def toString(self):
        return("Tipo Item = " + self.tipoItem 
            + " Id = " + self.id
            + " Descripcion = " + self.descripcion
            + " Valor Unidad = " + self.valorUnidad)
