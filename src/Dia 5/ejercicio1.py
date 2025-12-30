
"""
Crea una función devolver_distintos que reciba 3 integers como parámetros.
Suma los tres valores y evalúa el resultado obtenido.
Si la suma es mayor a 15, la función debe devolver el número mayor.
Si la suma es menor a 10, debe devolver el número menor.
Si la suma está entre 10 y 15 (inclusive), devuelve el valor intermedio.
"""

def numero_mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3
def numero_menor(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3 and num2 < num1:
        return num2
    else:
        return num3


def numero_intermedio(num1, num2, num3):
    # Verificamos si num1 está en medio
    if (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    # Verificamos si num2 está en medio
    elif (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    # Si no son los anteriores, por descarte es num3
    else:
        return num3

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    mayor = numero_mayor(num1, num2, num3)
    menor = numero_menor(num1, num2, num3)
    intermedio = numero_intermedio(num1, num2, num3)
    print(mayor, menor, intermedio)
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return intermedio

print(devolver_distintos(1, 3, 8))

# ---

def devolver_distintos2(a, b, c):
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]  # Retorna el intermedio

print("----------------------------")

# Pruebas
print(devolver_distintos2(10, 5, 2))  # Suma 17 (>15) -> Devuelve 10 (mayor)
print(devolver_distintos2(2, 2, 2))  # Suma 6  (<10) -> Devuelve 2  (menor)
print(devolver_distintos2(4, 5, 3))  # Suma 12 (10-15) -> Devuelve 4 (intermedio)
