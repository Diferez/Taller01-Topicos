class Cliente:
    #Constructor de cliente
    def __init__(self, nombre, apellido, id, genero, estadoCivil, fechaNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.genero = genero
        self.estadoCivil = estadoCivil
        self.fechaNacimiento = fechaNacimiento
        
    #Getter del cliente
    def getCliente(self):
        return self.nombre, self.apellido, self.id, self.genero, self.estadoCivil, self.fechaNacimiento

    #Setter del cliente
    def setCliente(nombre, apellido, id, genero, estadoCivil, fechaNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.genero = genero
        self.estadoCivil = estadoCivil
        self.fechaNacimiento = fechaNacimiento
    #toString para mostrar todo ordenado
    def toString(self):
        print("Nombre: " + self.nombre 
            + " Apellido: " + self.apellido
            + " id: " + self.id
            + " Genero: " + self.genero
            + " Estado Civil: " + self.estadoCivil
            + " Fecha de Nacimiento: " + self.fechaNacimiento) 

#Descomentarpara probar la creacion del cliente
#a =  Cliente("a","a","a","a","a","a")
#print(a.toString())