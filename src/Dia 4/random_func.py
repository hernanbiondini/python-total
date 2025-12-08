



from random import *

aleatorio = randint(0, 100)
print(aleatorio)


aleatorio = round(uniform(0, 100), 1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores =   ['azul', 'verde', 'amarillo', 'celeste']
aleatorio = choice(colores)
print(aleatorio)

numeros =  list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

