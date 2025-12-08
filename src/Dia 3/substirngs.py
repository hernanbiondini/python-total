
# CDE
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)

# FGHIJKLM
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]
print(fragmento)

# ABCDE
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)

# CEGI
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]   # slicing con paso -1 → invierte toda la cadena
print(resultado)