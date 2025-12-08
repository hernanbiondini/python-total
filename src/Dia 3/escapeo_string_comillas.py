# Ejemplos de escape de comillas en Python

# 1. Comillas dobles dentro de una cadena con comillas dobles
texto1 = "Ella dijo: \"Hola, Hernán\""

# 2. Comillas simples dentro de una cadena con comillas simples
texto2 = 'El perro se llama \'Lola\''

# 3. Mezclar comillas sin necesidad de escapar
texto3 = "El perro se llama 'Lola'"
texto4 = 'Ella dijo: "Hola, Hernán"'

# 4. Cadena multilinea con triple comilla (permite ambas sin escapar)
texto5 = """Esto contiene 'comillas simples' y "comillas dobles" sin escapar"""

# 5. Usar raw strings (aunque las comillas sí deben escaparse)
texto6 = r"Ruta en Windows: C:\\Users\\Hernan"

print(texto1)
print(texto2)
print(texto3)
print(texto4)
print(texto5)
print(texto6)
