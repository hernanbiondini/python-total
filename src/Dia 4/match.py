serie = "N-02"

if serie == "N-01":
    print("Sansung")

if serie == "N-02":
    print("Nokia")

elif serie == "N-03":
    print("Notorola")
else:
    print("No existe ese producto")

serie = "N-03"
match serie:
    case "N-01":
        print("Sansung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Notorola")
    case _:
         print("No existe ese producto")

cliente = {'nombre': 'Hernan',
           'edad':42,
           'ocupacion' : 'developer'}

pelicula = {'titulo':'Matrix',
            'ficha_tecnica':{'protagonista':'Keanu Reeves',
                             'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']


for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print(f'Esto es un cliente: {nombre} - {edad} - {ocupacion}')
        case {'titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print(f'Esto es un pelicula: {titulo} - {protagonista} -{director}')
        case _:
            print(f"Esto es otra cosa: {e}")
