


palabra = 'python'
lista = [letra for letra in palabra]
print(lista)

lista = [n for n in range(0, 21, 2)]
print(lista)


lista = [n/2 for n in range(0, 21, 2)]
print(lista)

lista = [n if n*2 > 10 else 'no' for n in range(0, 21, 2) ]
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = []
for val in valores:
    if  val % 2== 0:
        valores_pares.append(val)
print(valores_pares)

valores_pares = [valor for valor in valores if valor % 2 == 0]