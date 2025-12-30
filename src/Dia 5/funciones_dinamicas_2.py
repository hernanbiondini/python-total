from random import shuffle, randint  # Importamos las funciones específicas

# lista inicial --------------------------------------------------------------
palitos = ['-', '--', '---', '----']


# mezclar palitos --------------------------------------------------------------
def mezclar(lista):
    shuffle(lista)  # Ya no necesitas poner random.shuffle
    return lista


# pedirle intento --------------------------------------------------------------
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Introduce un número del 1 al 4: ")
    return int(intento)


# comprobar intento --------------------------------------------------------------
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("¡A lavar los platos!")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado el palito: {lista[intento - 1]}")


# --- Ejecución del juego de los palitos ---
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

# --------------------------------------------------------------

print("\n--- Lanzar dados ---")


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

def evaluar_jugada(d1, d2):
    return d1 + d2

d1, d2 = lanzar_dados()
suma_dados = evaluar_jugada(d1, d2)

if suma_dados  < 6:
    print(f"La suma de tus dados es {suma_dados}. Lamentable")
elif suma_dados  > 6 and suma_dados < 10:
    print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
else:
    print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")



# --------------------------------------------------------------

lista_numeros = [1,2,3,4,5,6,7,8,9,9]

def reducir_lista(lista_numeros):
    lista_sin_duplicados = list(set(lista_numeros))
    if lista_sin_duplicados:
        maximo = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(maximo)
    return lista_sin_duplicados

def promedio(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)

lista = reducir_lista(lista_numeros)
print(lista)
print(f"El promedio es {promedio(lista)}")

# --------------------------------------------------------------

print("Lanzar moneda")

def lanzar_moneda():
    resultado =  randint(1, 2)
    if resultado == 1:
        return "Cara"
    else :
        return "Cruz"

print(lanzar_moneda())

def probar_suerte(resultado_lanzamiento, lista_numeros):
    if resultado_lanzamiento == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros

mon = lanzar_moneda()
lista = probar_suerte(mon, lista_numeros)

print(lista)