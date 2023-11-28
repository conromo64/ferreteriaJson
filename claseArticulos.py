class articulo(object):

    ## definicion de las propiedades de la clase y asignación de valores por omisión
    ## constructor de la clase cliente 
    def __init__(self,claveArticulo,descripcion,costo,precioMayoreo,precioMenudeo,existenciaAlmacen,existenciaPisoVenta):
        self.claveArticulo = claveArticulo
        self.descripcion = descripcion
        self.costo = costo
        self.precioMayoreo = precioMayoreo
        self.precioMenudeo = precioMenudeo
        self.existenciaAlmacen = existenciaAlmacen
        self.existenciaPisoVenta = existenciaPisoVenta

    ## Definición de metodos de asignación para las propiedades de la clase
    def setClaveArticulo(self,claveArticulo):
        self.claveArticulo=claveArticulo
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    def setCosto(self,costo):
        self.costo = costo
    def setPrecioMayoreo(self,precioMayoreo):
        self.precioMayoreo = precioMayoreo
    def setPrecioMenudeo(self, precioMenudeo):
        self.precioMenudeo = precioMenudeo 
    def setExistenciaAlmacen(self, existenciaAlmacen):
        self.existenciaAlmacen = existenciaAlmacen 
    def setExistenciaPisoVenta(self, precioMenudeo):
        self.existenciaPisoVenta = existenciaPisoVenta

    ## metodos para extraer el valor de una propiedad en un objeto
    def getClaveArticulo(self):
        return self.claveArticulo
    def getDescripcion(self):
        return self.descripcion
    def getCosto(self):
        return self.costo
    def getPrecioMayoreo(self):
        return self.precioMayoreo
    def getPrecioMenudeo(self):
        return self.precioMenudeo 
    def getExistenciaAlmacen(self):
        return self.existenciaAlmacen 
    def getExistenciaPisoVenta(self):
        return self.existenciaPisoVenta


def altaArticulo(articulos,tipoArticulos):
    import claseTipoArticulos
    auxClaveArticulo = int(input("dame la clave "))
    auxDescripcion = input("dame el descripcion ")
    auxCosto = float(input("dame el costo "))
    auxPrecioMayoreo = float(input("dame el precio de mayoreo "))
    auxPrecioMenudeo = float(input("dame el precioMenudeo de menudeo "))
    auxExistenciaAlmacen = int(input("dame la existencia en almacen "))
    auxExistenciaPisoVenta = int(input("dame la existencia en piso "))
    # Imprime los tipos de articulo existentes
    claseTipoArticulos.impTipoArticulo(tipoArticulos)
    #lee el tipo de articulo 
    auxClaveTipoArticulo = int(input("dame el tipo de articulo "))
    #valida el tipo de articulo 
    while (claseTipoArticulos.buscaTipoArticulo(auxClaveTipoArticulo,tipoArticulos) == -1):
        print("******************tipo de articulo inexistente")
        auxClaveTipoArticulo = int(input("dame el tipo de articulo "))



    articulos.append(articulo(auxClaveArticulo,auxDescripcion,auxCosto,auxPrecioMayoreo,auxPrecioMenudeo,auxExistenciaAlmacen,auxExistenciaPisoVenta))
    return articulos

def impArticulo(articulos):
    for ind in range(0,len(articulos),1):
        indTipoArticulo=claseTipoArticulos.buscaTipoArticulo(auxClaveTipoArticulo,tipoArticulos)
        print(articulos[ind].getClaveArticulo(),"--",articulos[ind].getDescripcion(),"--",articulos[ind].getCosto(),"--",articulos[ind].getPrecioMayoreo(),"--",articulos[ind].getPrecioMenudeo(),articulos[ind].getExistenciaAlmacen(),articulos[ind].getExistenciaPisoVenta())


def buscaArticulo(auxClaveArticulo,articulos):
    indice=-1
    for ind in range(0,len(articulos),1):
        if (articulos[ind].getClaveArticulo()==auxClaveArticulo):
            indice=ind
    return indice 

def modificaArticulo(articulos):
    impArticulo(articulos)
    modClaveArticulo=int(input("dame la clave del cliente a modificar "))
    ind=buscaArticulo(modClaveArticulo) 
    if (ind!=-1):
        auxClaveArticulo = input("clave "+str(articulos[ind].getClaveArticulo())+" <- ")
        auxDescripcion = input("descripcion "+str(articulos[ind].getDescripcion())+" <- ")
        auxCosto = input("costo "+str(articulos[ind].getCosto())+" <- ")
        auxPrecioMayoreo = input("precio mayoreo "+str(articulos[ind].getPrecioMayoreo())+" <- ")
        auxPrecioMenudeo = input("precio menudeo"+str(articulos[ind].getPrecioMenudeo())+" <- ")
        auxExistenciaAlmacen = input("Existencia de almacen"+str(articulos[ind].getExistenciaAlmacen())+" <- ")
        auxExistenciaPisoVenta = input("Existencia de piso de venta "+str(articulos[ind].getExistenciaPisoVenta())+" <- ")

        articulos[ind].setClaveArticulo(auxClave)
        articulos[ind].setDescripcion(auxdescripcion)
        articulos[ind].setCosto(auxcosto)
        articulos[ind].setPrecioMayoreo(auxprecioMayoreo)
        articulos[ind].setPrecioMenudeo(auxprecioMenudeo)
        articulos[ind].setExistenciaAlmacen(auxExistenciaAlmacen)
        articulos[ind].setExistenciaPisoVenta(auxExistenciaPisoVenta)
        return articulos