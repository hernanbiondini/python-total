


mi_set = set([1,2,3,4,5,5])
print(type(mi_set))
print(mi_set)

# Los sets no permiten elementos duplicados
# Los set admiten elementos inmutables como tuplas
otro_set = {4,5,6,7,8,(1,2,3)}
print(type(otro_set))
print(otro_set)

print(1 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.remove(2)
print(s1)

s1.discard(10)  # No genera error si el elemento no existe
print(s1)

# Pop elimina y retorna un elemento aleatorio
s1.pop()
print(s1)

s1.clear()
print(s1)   