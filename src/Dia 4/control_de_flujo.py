
# <>

numero = 10

if numero > 100 :
    print("Es mayor a 100")
elif numero > 50 :
    print("Es mayor a 50")
else:
    print("Es menor a ambos")




num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))



if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif  num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1}  y {num2} son iguales")


habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")