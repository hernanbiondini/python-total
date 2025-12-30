


def saludar_persona(nombre):
    '''
    Esta funcion sirve para saludar a las personas
    '''
    print(f"Hola {nombre}")

saludar_persona("Hernan")

#------------------------

def multiplicar(x,y):
    return x*y
resultado = multiplicar(10,20)
print(resultado)

#------------------------

def invertir_palabra(palabra_original):
  palabra_invertida = palabra_original[::-1]
  palabra_final = palabra_invertida.upper()
  return palabra_final

palabra = "HolaMundo"
resultado = invertir_palabra(palabra)
print(f"La palabra original es: '{palabra}'")
print(f"El resultado de invertir y poner en mayúsculas es: '{resultado}'")
