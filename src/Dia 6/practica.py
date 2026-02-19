
from os import system

from pathlib import Path
ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)
system('cls')
print("hernan biondni")

def imprimir(archivo):
    archivo = open(archivo, "r")
    print(archivo.read())
    archivo.close()

# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer(archivo):
    mi_archivo2 = open(archivo, "r")
    return mi_archivo2.read()

abrir_leer("prueba.txt")

imprimir("prueba.txt")

# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
def sobrescribir(archivo):
    archivo = open(archivo, "w")
    archivo.write("contenido eliminado")
    archivo.close()

sobrescribir("prueba.txt")

imprimir("prueba.txt")


# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
def registro_error(archivo):
    archivo = open(archivo, "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()

registro_error("prueba.txt")

imprimir("prueba.txt")

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta) # C:\Users\Usuario
