from io import open

texto = 'holas'

archivo = open('gestion_de_archivos/hola-archivo.txt', 'w')

archivo.write(texto)
archivo.close()