from DAO.FacturaDao import FacturaDao
from Item.ItemPesoImpl import ItemPesoImpl
from Item.ItemImpl import ItemImpl
import json
class FacturaDaoImpl(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FacturaDaoImpl, cls).__new__(cls)
        return cls.instance
    
    
    def inicializar(self):
        self.facturas = []
        self.consec = 0
        self.items = []
        self.llenarItems()
    
    def llenarItems(self):
        self.items = []
        lista = self.verItems()
        itemsPeso = [5,6,7]
        for x in lista:
            if x['tipoItem'] in itemsPeso:
                self.items.append(ItemPesoImpl(x['tipoItem'],x['id'],x['descripcion'],x['valorUnidad']))
            else: 
                self.items.append(ItemImpl(x['tipoItem'],x['id'],x['descripcion'],x['valorUnidad']))

    def actualizarFactura(self, factura):
        for x in self.facturas:
            if x.getNro() == factura.getNro:
                x = factura
                break
    
    def eliminarFactura(self, factura):
        self.facturas.remove(factura)
    


    def crearTipoItems(self, TipoItem):
        js = {'id_tipoitem':TipoItem.id_tipoitem,'descripcion':TipoItem.descripcion}


        with open("jsons/TipoItem.json", "r+") as file:
            data = json.load(file)
            data.append(js)
            file.seek(0)
            json.dump(data,file,indent=4)
    
    def verTipoItems(self):

        with open('jsons/TipoItem.json') as file:
            data = json.load(file)
        
        return data

    def crearClientes(self, Cliente):
        js = {'nombre':Cliente.nombre,'apellido':Cliente.apellido,
            'id': Cliente.id, 'genero':Cliente.genero, 'estadoCivil':Cliente.estadoCivil,
            'fechaNacimiento': Cliente.fechaNacimiento}


        with open("jsons/Clientes.json", "r+") as file:
            data = json.load(file)
            data.append(js)
            file.seek(0)
            json.dump(data,file,indent=4)

    def verClientes(self):

        with open('jsons/Clientes.json') as file:
            data = json.load(file)
        
        return data

    def crearItems(self, Item):

        js = {'tipoItem':Item.tipoItem,'id':Item.id, 'descripcion':Item.descripcion, 'valorUnidad':Item.valorUnidad}


        with open("jsons/Items.json", "r+") as file:
            data = json.load(file)
            data.append(js)
            file.seek(0)
            json.dump(data,file,indent=4)
        
        self.llenarItems()

    def verItems(self):

        with open('jsons/Items.json') as file:
            data = json.load(file)
        
        return data
    
    def crearFactura(self, Item):

        js = {'tipoItem':Item.tipoItem,'id':Item.id, 'descripcion':Item.descripcion, 'valorUnidad':Item.valorUnidad}


        with open("jsons/Facturas.json", "r+") as file:
            data = json.load(file)
            data.append(js)
            file.seek(0)
            json.dump(data,file,indent=4)
        
        self.llenarItems()
    
    def verFacturas(self):

        with open('jsons/Facturas.json') as file:
            data = json.load(file)
        
        return data