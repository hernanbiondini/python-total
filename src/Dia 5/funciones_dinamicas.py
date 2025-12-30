

def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(111)
print(resultado)

def chequear_3_cifras_lista(lista):
    resultado = False
    for n in lista:
        if n in range(100, 1000):
            resultado = True
        else:
            pass
    return resultado

resultado = chequear_3_cifras_lista([11,22,33])
print(f"resultado {resultado}")

# --------------------------------------------------------------

def chequear_3_cifras_lista_agregar(lista):
    lista_3_cifras = []
    resultado = False
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append (n)
        else:
            pass
    return lista_3_cifras

print(f"Lista de 3 cifras: {chequear_3_cifras_lista_agregar([11,22,333,1,2,3,4,5,6,7,8,9])}")

# --------------------------------------------------------------

lista_numeros = [3,7,8-9]

def todos_positivos(lista):
    resultado = True
    for n in lista:
        if n  < 0:
            return False
    return resultado

res = todos_positivos([3,-7,8])
print(f"Todos positivos: {res}")

# --------------------------------------------------------------

def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(0, 1000):
            suma = suma + n
    return suma

print(suma_menores(lista_numeros))

# --------------------------------------------------------------

precios_cafe =[('caouchino',1.5),('expresso',1.2),('moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

precio_m, cafe_mc = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {precio_m} con un precio de {cafe_mc}")
