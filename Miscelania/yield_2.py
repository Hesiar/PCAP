'''funcion generadora'''
def potencias_de_2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2
        
for p in potencias_de_2(5):
    print(p)
    
'''alternativa (1) usando una lista por compresion'''
x= [p for p in potencias_de_2(5)]
print(x)

'''alternativa (2) usando la funcion list()'''
x = list(potencias_de_2(5))
print(x)