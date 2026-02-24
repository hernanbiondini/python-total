class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")

def animal_habla(animal):
    animal.hablar()

vaca1 = Vaca("Vaca")
oveja1 = Oveja("Oveja")

#animales = [vaca1, oveja1]
#for animal in animales:
#    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)
