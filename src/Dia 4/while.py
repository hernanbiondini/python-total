
# <>

monedas = 5

while monedas>0:
    print(f"Tengo {monedas} monedas")
    # monedas = monedas - 1
    monedas -= 1
else:print("No tengo monedas")

print("------------------------------------------")
respuesta = 's'
while respuesta=='s':
    respuesta = input("¿Quieres seguir? (s/n): ")
    if respuesta=='n':
        break

print("------------------------------------------")
rta = 's'
while rta=='s':
    rta = input("¿Quieres seguir? (s/n): ")
else:
    print("Gracias")

print("------------------------------------------")
r = 'n'
while r=='s':
   pass
else:
    print("Fin")

print("--------------pass------------------------")
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'r':
        pass
    print(letra)

print("--------------continue------------------------")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)

print("--------------break------------------------")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)