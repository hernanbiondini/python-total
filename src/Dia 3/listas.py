


mi_lista = ['a', 'b', 'c']
otra_lista = ['a', 'b', 'c', True]

print(type(mi_lista))
print(type(otra_lista))


print(len(mi_lista))

resultado = mi_lista[0]
print(resultado)

resultado = mi_lista[0:1]
print(resultado)


mi_lista2 = mi_lista + otra_lista
print(mi_lista2)


mi_lista2[2] = 'XXXX'
print(mi_lista2)

mi_lista2.append('zzz')
print(mi_lista2)

mi_lista2.pop()
print(mi_lista2)

pop = mi_lista2.pop(0)
print(mi_lista2)
print(pop)

lista = [3,6,2,8,1]
print(lista)
lista.sort()
print(lista)