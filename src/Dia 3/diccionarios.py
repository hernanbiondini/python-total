# diccionarios

diccionario = {'perro':'dog', 'gato':'cat'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['perro']
print(resultado)

print("--------------------")

cliente = {'nombre': 'Juan','apellido': 'Perez','peso': 88,'altura': 1.75}

consulta = cliente['apellido']
print(consulta)

dic = {'c1': 1, 'c2': [10,20,30], 'c3': {'s1':100, 's2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s2'])

print("--------------------")

dicc = {'c1': ['a','b','c'], 'c2': ['d','e','f']}
print(dicc['c2'][1].upper())

print("--------------------")
d ={1: 'a', 2: 'b'}
print(d)
d[3] = 'c'
print(d)
d[2] = 'B'
print(d)

print("--------------------")
print(d.keys())
print(d.values())
print(d.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])