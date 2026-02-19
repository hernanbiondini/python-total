
from pathlib import Path

#base = Path.home()
#guia = Path("Barcelona", "Sagrada_Familia.txt")
#print(base)
#print(guia)

#base = Path.home()
#guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")
#print(guia)
#print(guia2)
#print(guia.parent)

guia = Path(Path.home(), "Europa")
for file in Path(guia).glob('**/*.txt'):
    print(file)

# Desde el punto hacia abajo
guia2 = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
print(guia2)
en_europa = guia2.relative_to(Path("Europa"))
en_espania = guia2.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
