class cliente(object):

    ## definicion de las propiedades de la clase y asignación de valores por omisión
    ## constructor de la clase cliente 
    def __init__(self,clave,nombre,apPaterno,apMaterno,tipo):
        self.clave = clave
        self.nombre = nombre
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.tipo = tipo

    ## Definición de metodos de asignación para las propiedades de la clase
    def setClave(self,clave):
        self.clave=clave
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApPaterno(self,apPaterno):
        self.apPaterno = apPaterno
    def setApMaterno(self,apMaterno):
        self.apMaterno = apMaterno
    def setTipo(self, tipo):
        self.tipo = tipo 

    ## metodos para extraer el valor de una propiedad en un objeto
    def getClave(self):
        return self.clave
    def getNombre(self):
        return self.nombre
    def getApPaterno(self):
        return self.apPaterno
    def getApMaterno(self):
        return self.apMaterno
    def getTipo(self):
        return self.tipo 

def altaCliente(clientes):
    auxClave = int(input("dame la clave "))
    auxNombre = input("dame el nombre ")
    auxApPaterno = input("dame el apellido paterno ")
    auxApMaterno = input("dame el apellido materno ")
    auxTipo = input("dame el tipo de cliente ")
    clientes.append(cliente(auxClave,auxNombre,auxApPaterno,auxApMaterno,auxTipo))
    return clientes

def impClientes(clientes):
    for ind in range(0,len(clientes),1):
        print(clientes[ind].getClave(),"--",clientes[ind].getNombre(),"--",clientes[ind].getApPaterno(),"--",clientes[ind].getApMaterno(),"--",clientes[ind].getTipo())

def buscaCliente(auxclave,clientes):
    indice=-1
    for ind in range(0,len(clientes),1):
        if (clientes[ind].getClave()==auxclave):
            indice=ind
    return indice 

def modificaCliente(clientes):
    impClientes(clientes)
    modClave=int(input("dame la clave del cliente a modificar "))
    ind=buscaCliente(modClave,clientes) 
    if (ind!=-1):
        auxClave = input("clave "+str(clientes[ind].getClave())+" <- ")
        auxNombre = input("nombre "+str(clientes[ind].getNombre())+" <- ")
        auxApPaterno = input("apellido paterno "+str(clientes[ind].getApPaterno())+" <- ")
        auxApMaterno = input("apellido materno "+str(clientes[ind].getApMaterno())+" <- ")
        auxTipo = input("tipo "+str(clientes[ind].getTipo())+" <- ")
        clientes[ind].setClave(auxClave)
        clientes[ind].setNombre(auxNombre)
        clientes[ind].setApPaterno(auxApPaterno)
        clientes[ind].setApMaterno(auxApMaterno)
        clientes[ind].setTipo(auxTipo)
    return clientes
