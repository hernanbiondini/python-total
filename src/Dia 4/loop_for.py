
nombres = ['Victor', 'Hernán', 'Biondini']

for nombre in nombres:
    indice = nombres.index(nombre)
    print(f"Nombre: {nombre} - Indice: {indice}")
    if nombre.startswith('V'):
        print(f"Nombre: {nombre}")

# lista de numeros de 1 a 5
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)


palabra = 'hernan'
for letra in palabra:
    print(letra)

for objeto in[[1,2],[3,4],[5,6]]:
    print(objeto)

print("--------------------------------------")

for objeto in[[1,2],[3,4],[5,6]]:
    for elemento in objeto:
        print(elemento)

print("--------------------------------------")
for objeto, elemento in[[1,2],[3,4],[5,6]]:
    print(objeto)
    print(elemento)

print("--------------------------------------")

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for item in dic:
    print(item)
print("--------------------------------------")

for item in dic.items():
    print(item)

print("--------------------------------------")

for value in dic.values():
    print(value)

print("--------------------------------------")

for a,b in dic.items():
    print(a,b)