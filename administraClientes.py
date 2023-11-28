import claseClientes

def admClientes(clientes):
    opcion = 'N'
    while opcion!='S':
        print("[A]lta de clientes")
        print("[I]mprime listado de clientes")
        print("[M]odifica un cliente")
        print("[S]alir")
        opcion=input().upper()
        if opcion=="A":
            clientes=claseClientes.altaCliente(clientes)
        elif opcion=="I":
            clientes=claseClientes.impClientes(clientes)
        elif opcion=="M":
            clientes=claseClientes.modificaCliente(clientes)
        elif opcion=="S":
            return clientes
        else:
            print("OPCION  INVALIDA!")        
