class TipoItem:
    def __init__(self, id_tipoitem, descripcion): #constructor de tipo item
        self.id_tipoitem = id_tipoitem 
        self.descripcion = descripcion 

    def getTipoItems(self): #retorna el tipo item
        return self.id_tipoitem


