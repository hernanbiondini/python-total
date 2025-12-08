


mi_tupla = (1, "hola", True, 4.3,( 10,20),1)
print(type(mi_tupla))
print(mi_tupla[2])
print(mi_tupla[4][0])
print("--------------------")

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

print("--------------------")

a,b,c,d,e,f = mi_tupla
print(a,b,c,d,e,f)
print("--------------------")
print(len(mi_tupla))
print(mi_tupla.count(1))

print("--------------------")

print(mi_tupla.index(1))