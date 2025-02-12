mi_lista = [x for x in range(11) if x % 2 == 0]
mi_generador = (x for x in range(11) if x % 2 == 0)

for v in mi_lista:
    print(v, end=" ")
print()

for v in mi_generador:
    print(v, end=" ")
print()