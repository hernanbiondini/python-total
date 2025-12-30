import random

palabras = [
        "python", "algoritmo", "computadora", "programacion", "teclado",
        "monitor", "servidor", "internet", "biblioteca", "variable",
        "diccionario", "bucle", "funcion", "objeto", "clase",
        "herencia", "interfaz", "escritorio", "navegador", "codigo",
        "universo", "galaxia", "estrella", "planeta", "telescopio",
        "horizonte", "aventura", "misterio", "fortaleza", "libertad",
        "justicia", "equilibrio", "silencio", "armonia", "creatividad",
        "entusiasmo", "paciencia", "sabiduria", "victoria", "esperanza",
        "elefante", "jirafa", "cocodrilo", "mariposa", "delfin",
        "orquesta", "guitarra", "acuarela", "escultura", "laberinto"
    ]

def es_valida_letra(letra):
    return (letra in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ") and (len(letra) == 1)

def jugar():
    palabra_secreta = random.choice(palabras).upper()
    print(f"La palabra tiene {len(palabra_secreta)} letras.")
    tablero = ["_"] * len(palabra_secreta)
    print(tablero)
    intentos_restantes = 6
    letras_probadas = []

    print("¡Bienvenido al Ahorcado!")


    # 2. Bucle principal del juego
    while intentos_restantes > 0 and "_" in tablero:
        print(f"\nPalabra: {' '.join(tablero)}")
        print(f"Letras probadas: {', '.join(letras_probadas)}")
        print(f"Intentos restantes: {intentos_restantes}")

        letra = input("Ingrese una letra: ")
        while not es_valida_letra(letra):
            print("Ingrese una letra valida")
            letra = input("Ingrese una letra: ")

        # Validaciones básicas
        #if len(letra) != 1 or not letra.isalpha():
        #    print("Por favor, introduce solo una letra válida.")
        #    continue

        if letra in letras_probadas:
            print("Ya habías probado esa letra. Intenta con otra.")
            continue

        letras_probadas.append(letra)

        # 3. Verificar si la letra está en la palabra
        if letra in palabra_secreta:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            # Actualizamos el tablero en todas las posiciones donde aparezca la letra
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    tablero[i] = letra
        else:
            print(f"Lo siento, la '{letra}' no está.")
            intentos_restantes -= 1

    # 4. Final del juego
    if "_" not in tablero:
        print(f"\n¡FELICIDADES! Ganaste. La palabra era: {palabra_secreta}")
    else:
        print(f"\nGAME OVER. Te quedaste sin intentos. La palabra era: {palabra_secreta}")

jugar()