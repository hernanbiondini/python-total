"""
Escribe una función que requiera una cantidad indefinida deargumentos.
Lo que hará esta función es devolver True
si enalgún momento se ha ingresado al numero
cero repetido dosveces consecutivas
.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def busca_00(*args):
    print(args)
    texto_tupla = ""
    for elemento in args:
        texto_tupla += str(elemento)
    print(texto_tupla)
    if texto_tupla.find("00") != -1:
        return True
    else:
        return False


print(busca_00(1,0,0,3,4,5,6, 0))