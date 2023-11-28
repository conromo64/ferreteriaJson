class tipoArticulo(object):

    ## definicion de las propiedades de la clase y asignación de valores por omisión
    ## constructor de la clase cliente 
    def __init__(self,claveTipoArticulo,descripcion):
        self.claveTipoArticulo = claveTipoArticulo
        self.descripcion = descripcion

    ## Definición de metodos de asignación para las propiedades de la clase
    def setClaveTipoArticulo(self,claveTipoArticulo):
        self.claveTipoArticulo=claveTipoArticulo
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    ## metodos para extraer el valor de una propiedad en un objeto
    def getClaveTipoArticulo(self):
        return self.claveTipoArticulo
    def getDescripcion(self):
        return self.descripcion


def altaTipoArticulo(tipoArticulos):
    auxclaveTipoArticulo = int(input("dame la clave "))
    auxDescripcion = input("dame el descripcion ")
    return tipoArticulos

def impTipoArticulo(tipoArticulos):
    for ind in range(0,len(tipoArticulos),1):
        print(tipoArticulos[ind].getClaveTipoArticulo(),"--",tipoArticulos[ind].getDescripcion())


def buscaTipoArticulo(auxClaveTipoArticulo,tipoArticulos):
    indice=-1
    print('la clave que buscas es ', auxClaveTipoArticulo)
    for ind in range(0,len(tipoArticulos),1):
        if (tipoArticulos[ind].getClaveTipoArticulo()==auxClaveTipoArticulo):
            indice=ind
    return indice 

def modificaTipoArticulo(tipoArticulos):
    impArticulo(tipoArticulos)
    modClaveTipoArticulo=int(input("dame la clave del tipo a modificar "))
    ind=buscaTipoArticulo(modClaveTipoArticulo) 
    if (ind!=-1):
        auxClaveTipoArticulo = input("clave "+str(tipoArticulos[ind].getclaveTipoArticulo())+" <- ")
        auxDescripcion = input("descripcion "+str(tipoArticulos[ind].getDescripcion())+" <- ")
        tipoArticulos[ind].setClaveTipoArticulo(auxClaveTipoArticulo)
        tipoArticulos[ind].setDescripcion(auxdescripcion)
        return tipoArticulos