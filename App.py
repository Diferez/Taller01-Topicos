from DAO.FacturaDaoImpl import FacturaDaoImpl
from deps.Factura import Factura
from Item.ItemFactura import ItemFactura
from datetime import date
from deps.Cliente import Cliente

def main():
    db = FacturaDaoImpl()
    db.inicializar()

    #Opciones del usuario
    print("1. Para crear factura")
    print("2. Para modificar factura")
    print("3. Para eliminar factura")
    print("4. para ver facturas")
    print("5. para salir")

    entrada = int(input(""))

    if entrada == 1:
        crear()
    elif entrada == 2:
        modificar()
    elif entrada == 3:
        eliminar()
    elif entrada == 4:
        ver()
        
    elif entrada == 5:
        salir()
#Crear una factura nueva4
def crear():
    print("Ingresa el estado de la factura")
    print("Estado Pendiente = 0 | Estado Pagado = 1")
        
    val = input()
    if(val == '0' ):
        estado = "pendiente"
    else:
        estado = "pagado"
    print(estado)

    
    mostrarcliente()


    

    #newDate = date(año, mes, dia)
    
    #factura = Factura(5, estado, cliente)
    pass

def modificar():
    pass

def ver():
    print("Viendo Facturas")
    db = FacturaDaoImpl()
    facturas = db.verFacturas()
    for factura in facturas:
        print(factura.toString())
    pass
def eliminar():
    pass
def salir():
    print("Bye")
    pass

def mostrarcliente():
    print("# Lista de Clientes #")
    cdb = FacturaDaoImpl()
    clientes = cdb.verClientes()
    print("ID        Nombre")
    for cliente in clientes:
        #print(cliente)
        print(cliente['id'],cliente['nombre'])
    pass
    print("-----------------")
    print("Seleccionar id del cliente que busca, de lo contrario poner ' new '")
    idU = input()
    for client in clientes:
        if idU == client:
            return idU
    idU = crearcliente()
    return idU
    

def crearcliente():
    #Crear un cliente
    print("# Datos del cliente #")
    print("Nombre cliente: ")
    nombre = input()
    print("Apellido cliente: ")
    apellido = input()
    print("Id cliente: ")
    idc = input()
    print("Genero cliente: ")
    gen = input()
    print("Estado Civil: ")
    estadoc = input()
    print("Fecha de nacimiento: ")
    FechaN = input()

    ndb = FacturaDaoImpl()
    ncliente = ndb.CrearClientes()

    ncliente = Cliente(nombre, apellido, idc, gen, estadoc, FechaN)

    return idc
        



if __name__ == "__main__":
    main()