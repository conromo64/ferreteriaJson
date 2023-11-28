def leeArchivo(ruta):
    #abre el archivo en solo lectura
    with open(ruta, 'r') as archivo:
        #elimina el salto de linea 
        datos = [dato.rstrip('\n') for dato in archivo.readlines()]
    archivo.close()
    return datos 

def borraArchivo(ruta):
    from pathlib import Path
    archivo = Path(ruta)
    if archivo.is_file():
        archivo.unlink()
        print(f'El archivo "{ruta}" ha sido borrado.')
    else:
        print(f'El archivo "{ruta}" no existe.')

def creaArchivo(ruta,datos):
    borraArchivo(ruta)
    #abre el archivo en forma de escritura
    with open(ruta, 'w') as archivo:
        #descarga los dato en el archivo
        for dato in datos:     
            archivo.write(dato+"\n")
    print(f"Se ha creado el archivo '{ruta}' con éxito.")



