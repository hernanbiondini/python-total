class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro volo {metros}")

mi_pajaro = Pajaro('red', 'tucan')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
mi_pajaro.color = 'blue'
print(mi_pajaro.color)

mi_pajaro2 = Pajaro('amarillo', 'tucan')
print(mi_pajaro2.color)
print(mi_pajaro2.alas)
mi_pajaro2.piar()
mi_pajaro2.volar(5)
