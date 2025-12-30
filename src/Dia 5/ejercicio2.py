"""
Escribe una función que reciba cualquier palabra como parámetro,
y quedevuelva todas sus letras únicas
(sin repetir) pero en ordenalfabético.
Por ejemplo si al invocar esta función pasamos la palabra"entretenido",
debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""

def procesar_string(palabra):
    letras_unicas = set(palabra)
    letras_ordenadas = sorted(letras_unicas)
    print(letras_unicas)
    print(letras_ordenadas)

procesar_string("hernan")