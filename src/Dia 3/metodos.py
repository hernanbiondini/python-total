
texto = "Texto de prueba"
resultado = texto

resultado = texto.upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

resultado = texto.find("t")
print(resultado)

resultado = texto.find("z")
print(resultado)

resultado = texto.replace("prueba", "producción")
print(resultado)

resultado = texto.replace("e", "x")
print(resultado)
