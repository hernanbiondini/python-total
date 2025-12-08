
# <>
mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool = 4 < 5 and 5 < 6
print(mi_bool)

mi_bool = 4 < 5 or 5 < 1
print(mi_bool)


texto = "esta frase es breve"

mi_bool = 'frase' in texto
print(mi_bool)

mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

mi_bool = not 4 < 5 < 6
print(mi_bool)
