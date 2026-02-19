import os

#ruta = os.getcwd()
#print(ruta)

#otra_ruta = os.chdir('C:\\Users\\Hbiondini\\Desktop')
#archivo = open('lalala.txt')
#print(archivo.read())

# ruta = os.makedirs('C:\\Users\\Hbiondini\\Desktop\\Notas')

ruta ='C:\\Users\\Hbiondini\\Desktop\\Notas\\lalala.txt'
basename = os.path.basename(ruta)
dirname = os.path.dirname(ruta)
spl = dirname.split(ruta)
print(basename)
print(dirname)
print(spl)
