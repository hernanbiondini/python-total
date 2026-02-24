class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('red', 'tucan')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
mi_pajaro.color = 'blue'
print(mi_pajaro.color)

mi_pajaro2 = Pajaro('amarillo', 'tucan')
print(mi_pajaro2.color)
print(mi_pajaro2.alas)
