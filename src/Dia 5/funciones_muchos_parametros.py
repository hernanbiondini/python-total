

def suma(a,b):
    return a+b

print(suma(6,6))


def suma_multiple(*args):
    total = 0
    for arg in args:
        total += arg
    #return sum(args)
    return total

print(suma_multiple(3,3,3,3))
print(suma_multiple(3,3,3))

# ----------------------------------

def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg * arg
    return total

print(suma_cuadrados(3,3,3))

# ----------------------------------

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

print(numeros_persona("Hernán",6,3))

# ----------------------------------



