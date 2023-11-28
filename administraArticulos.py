import claseArticulos

def admArticulos(articulos,tipoArticulos):
    opcion = 'N'
    while opcion!='S':
        print("[A]lta de articulos")
        print("[I]mprime articulos")
        print("[M]odifica un articulo")
        print("[S]alir")
        opcion=input().upper()
        if opcion=="A":
            articulos = claseArticulos.altaArticulo(articulos,tipoArticulos)            
        elif opcion=="I":
            claseArticulos.impArticulo(articulos)
        elif opcion=="M":
            articulos = claseArticulos.modificaCliente(articulos)
        elif opcion=="S":
            return articulos
        else:
            print("OPCION  INVALIDA!")     