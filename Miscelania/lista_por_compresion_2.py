'''Lista por compresion (2)'''
mi_lista = []

# Lista de pares entre 1 y 10
for x in range(11):
    mi_lista.append(x % 2)
    
print(mi_lista)

# idem pero por compresion
mi_lista = [x % 2 for x in range(11)]
print(mi_lista)