# Modos de apertura de archivos

# 'R' (lectura): Abre el archivo solo para lectura. No se puede escribir en él; si intentas hacerlo, se generará un error.
# 'W' (escritura): Abre el archivo para escribir. Si el archivo ya existe, este modo lo vacía, así que se perderá todo su
#       contenido anterior. Este modo se utiliza para crear un nuevo archivo o sobrescribir uno existente.
# 'A' (apéndice): Abre el archivo para agregar contenido al final del mismo. A diferencia del modo 'W',
#       el contenido original se mantiene, lo que lo hace útil para registrar actividades sin eliminar datos anteriores.


# archivo = open('prueba.txt','a')
# archivo.write('soy hernandez')
# archivo.close()

archivo = open('prueba1.txt','w')
archivo.write('La caída de los gigantes es una novela del escritor Ken Follett que fue publicada el 28 de septiembre de 2010 de manera simultánea en todo el mundo. La tirada inicial fue de 2,5 millones de ejemplares\n')
archivo.write('Es la primera parte de una serie llamada Trilogía del siglo, a través de la cual es posible acercarse a los principales acontecimientos del siglo XX, incluyendo la I Guerra Mundial, la II Guerra Mundial y la Guerra Fría\n')
archivo.close()

archivo = open('prueba2.txt','w')
archivo.write('''La caída de los gigantes es una novela del 
escritor Ken Follett que fue publicada el 28 de septiembre de 2010 de manera 
simultánea en todo el mundo. La tirada inicial fue de 2,5 millones de ejemplares''')
archivo.close()

archivo = open('prueba3.txt','w')
#archivo.writelines(['hola','mundo'])
lista = ['hola','mundo']
for p in lista:
    archivo.write(p+'\n')
archivo.close()