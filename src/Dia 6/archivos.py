


mi_archivo = open("prueba.txt", "r")
print(mi_archivo)
print(mi_archivo.read())
mi_archivo.close()


print("")
mi_archivo2 = open("prueba.txt", "r")
una_linea = mi_archivo2.readline()
print(una_linea)
mi_archivo2.close()


print("")
mi_archivo3 = open("prueba.txt", "r")
una_linea2 = mi_archivo3.readline()
print(una_linea2.upper())

una_linea2 = mi_archivo3.readline()
print(una_linea2)

una_linea2 = mi_archivo3.readline()
print(una_linea2)

mi_archivo3.close()

print("")
mi_archivo4 = open("prueba.txt", "r")
for l in mi_archivo4:
    print("Aqui dice: " + l)
mi_archivo4.close()


print("")
mi_archivo5 = open("prueba.txt", "r")
todas = mi_archivo5.readlines()
print(todas)
mi_archivo5.close()

print("")
mi_archivo6 = open("prueba.txt", "r")
indice = 1
for l in mi_archivo6:
    if indice == 2:
        print(l)
    indice += 1
mi_archivo6.close()