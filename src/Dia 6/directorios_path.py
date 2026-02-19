
from libreria_pathlib import Path

carpeta = Path('/Users/Hbiondini/Desktop/Notas')
archivo = carpeta / 'lalala.txt'

mi_archivo = open(archivo, 'r')
print(mi_archivo.read())