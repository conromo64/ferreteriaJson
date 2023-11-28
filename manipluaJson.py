def creaJsonArticulo(listaArticulos):
    import json
    import claseArticulos
    import manipulaArchivo
    lista = []
    for articulo in listaArticulos:
        jsonStr = '{'
        jsonStr = jsonStr+'"claveArticulo" : '+str(articulo.getClaveArticulo())+','
        jsonStr = jsonStr+'"descripcion"  : "'+str(articulo.getDescripcion())+'",'
        jsonStr = jsonStr+'"costo" : '+str(articulo.getCosto())+','
        jsonStr = jsonStr+'"precioMayoreo" : '+str(articulo.getPrecioMayoreo())+','
        jsonStr = jsonStr+'"precioMenudeo" : '+str(articulo.getPrecioMenudeo())+','
        jsonStr = jsonStr+'"existenciaAlmacen" : '+str(articulo.getExistenciaAlmacen())+','
        jsonStr = jsonStr+'"existenciaPisoVenta" : '+str(articulo.getExistenciaPisoVenta())+'}'
        lista.append(jsonStr)
    ruta = r"C:\cetis155\semestres\Ago 23 Ene 24\materias\Prog 3 semestre\codigos\ferreteria\datos\articulo.txt"
    manipulaArchivo.creaArchivo(ruta,lista) 

def leeJsonArticulos():
    import json
    import claseArticulos
    import manipulaArchivo
    ruta = r"C:\cetis155\semestres\Ago 23 Ene 24\materias\Prog 3 semestre\codigos\ferreteria\datos\articulo.txt"
    lineas = manipulaArchivo.leeArchivo(ruta)
    datos = [] 
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxClaveArticulo = jsonDict['claveArticulo']
        auxDescripcion = jsonDict['descripcion']
        auxCosto = jsonDict['costo']
        auxPrecioMayoreo = jsonDict['precioMayoreo']
        auxPrecioMenudeo = jsonDict['precioMenudeo']
        auxExistenciaAlmacen = jsonDict['existenciaAlmacen']
        auxExistenciaPisoVenta = jsonDict['existenciaPisoVenta']
        datos.append(claseArticulos.articulo(auxClaveArticulo,auxDescripcion,auxCosto,auxPrecioMayoreo,auxPrecioMenudeo,auxExistenciaAlmacen,auxExistenciaPisoVenta))
    
    return datos
    
##########################################
#  TIPO DE ARTICULO
##########################################

def creaJsonTipoArticulo(listaTipoArticulos):
    import json
    import claseTipoArticulos
    import manipulaArchivo
    lista = []
    for tipoArticulo in listaTipoArticulos:
        jsonStr = '{'
        jsonStr = jsonStr+'"tipoArticulo" : '+str(articulo.getClaveTipoArticulo())+','
        jsonStr = jsonStr+'"descripcion"  : "'+str(articulo.getDescripcion())+'",'
        lista.append(jsonStr)
    ruta = r"C:\cetis155\semestres\Ago 23 Ene 24\materias\Prog 3 semestre\codigos\ferreteria\datos\tipoArticulo.txt"
    manipulaArchivo.creaArchivo(ruta,lista) 

def leeJsonTipoArticulos():
    import json
    import claseTipoArticulos
    import manipulaArchivo
    ruta = r"C:\cetis155\semestres\Ago 23 Ene 24\materias\Prog 3 semestre\codigos\ferreteria\datos\tipoArticulo.txt"
    lineas = manipulaArchivo.leeArchivo(ruta)
    datos = [] 
    for linea in lineas:
        jsonDict = json.loads(linea)
        auxTipoArticulo = jsonDict['tipoArticulo']
        auxDescripcion = jsonDict['descripcion']
        datos.append(claseTipoArticulos.tipoArticulo(auxTipoArticulo,auxDescripcion))
    
    return datos
