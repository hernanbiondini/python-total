

# Entradas
texto = input("Ingrese un texto: ")
texto_mayusculas = texto.upper()

# Formateos
letras = input("Ingrese 3 letras separadas por comas: ")
letras_mayusculas = letras.upper()
letras_mayusculas_lista = letras_mayusculas.split(",")
primera_letra, segunda_letra, tercera_letra = letras_mayusculas_lista
print(primera_letra, segunda_letra, tercera_letra)

# Punto 1
primera_letra_count = texto_mayusculas.count(primera_letra)
print(f"La letra {primera_letra} se encuentra {primera_letra_count} veces")
segunda_letra_count = texto_mayusculas.count(segunda_letra)
print(f"La letra {segunda_letra} se encuentra {segunda_letra_count} veces")
tercera_letra_count = texto_mayusculas.count(tercera_letra)
print(f"La letra {tercera_letra} se encuentra {tercera_letra_count} veces")

# Punto 2
palabras = texto_mayusculas.split(" ")
print(f"El texto tiene {len(palabras)} palabras")

# Punto 3
print(f"La primera letra del texto es {texto_mayusculas[0]}")
print(f"La última letra del texto es {texto_mayusculas[-1]}")

# Punto 4
print(f"Texto invertido {texto[::-1]}")

# Punto 5
python = "Python" in texto
print(f"La palabra \"Python\" se encuentra en el texto: {python}")