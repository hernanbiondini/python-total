import math



def es_primo(n):
    if n < 2:
        return False
    if n ==  2:
        return True
    if n % 2 == 0:
        return False

    # Para n impar mayor que 2 → divide n entre todos los números impares desde 3 hasta √n.
    # Si alguno lo divide exactamente (resto = 0), no es primo. Si ninguno lo divide, es primo.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True



def contar_primos(numero):
    contador = 0
    for numero in range(1, numero + 1):
        if es_primo(numero):
            contador += 1
    return contador

numero = int(input("Ingrese un numero: "))
print(f"Cantidad de numeros primos entre 0 y {numero}: {contar_primos(numero)}")