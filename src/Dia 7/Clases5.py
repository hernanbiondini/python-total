class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro volo {metros}")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(self.color)


    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} de huevos")
        cls.alas = False


    @staticmethod
    def mirar():
        print("El pajaro miraa")

mi_pajaro = Pajaro('red', 'tucan')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
mi_pajaro.color = 'blue'
print(mi_pajaro.color)

print('')

mi_pajaro2 = Pajaro('amarillo', 'tucan')
print(mi_pajaro2.color)
print(mi_pajaro2.alas)
mi_pajaro2.piar()
mi_pajaro2.volar(5)
mi_pajaro2.pintar_negro()
#mi_pajaro2.alas = False

print(mi_pajaro.alas)
print(mi_pajaro2.alas)

Pajaro.poner_huevos(5)

print(mi_pajaro.alas)
print(mi_pajaro2.alas)

Pajaro.mirar()