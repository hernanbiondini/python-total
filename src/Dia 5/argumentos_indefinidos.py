


def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y =5, z=2)

# -----------------------------------
def suma2(**kwargs):
    for k, v in kwargs.items():
        print(f"Clave: {k}, valor: {v}")

suma2(x=3, y =5, z=2)

# -----------------------------------
def suma3(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return total

print(suma3(x=3, y =5, z=2))

# -----------------------------------
def suma4(num1, num2, *args, **kwargs):
    print(f'el primer valor es {num1}, el segundo valor es {num2}')

    for arg in args:
        print(f"arg: {arg}")

    for k, v in kwargs.items():
        print(f"Clave: {k}, valor: {v}")

suma4(1,2, 7,8,9,x=3, y =5, z=2)

ar = [100, 200, 300]
kwar = {'x': 100, 'y': 200, 'z': 300}
suma4(15, 50, *ar, **kwar)

# -----------------------------------

def cantidad_atributos(*args, **kwargs):
    return len(kwargs.items()) + len(args)

resp = cantidad_atributos(1, "q", d=1, j=6)
print(f"Cantidad de parametros: {resp}")

# -----------------------------------

def cantidad_atributos( **kwargs):
    return list(kwargs.values())
print(f"Valores: {cantidad_atributos(a=1, b=2, c=3)}")

# -----------------------------------

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")