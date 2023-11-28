import claseTipoArticulos

def admTipoArticulos(tipoArticulos):
    opcion = 'N'
    while opcion!='S':
        print("[A]lta de tipo de articulos")
        print("[I]mprime tipo de articulos")
        print("[M]odifica un tipo de articulo")
        print("[S]alir")
        opcion=input().upper()
        if opcion=="A":
            tipoArticulos = claseTipoArticulos.altaTipoArticulo(tipoArticulos)            
        elif opcion=="I":
            claseTipoArticulos.impTipoArticulo(tipoArticulos)
        elif opcion=="M":
            tipoArticulos = claseTipoArticulos.modificaTipoCliente(tipoArticulos)
        elif opcion=="S":
            return tipoArticulos
        else:
            print("OPCION  INVALIDA!")  