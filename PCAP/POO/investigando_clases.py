
# Ejemplo de las propiedades de las introspeccion de la reflexion del lenguaje Python

class MyClass:
    pass

obj = MyClass()

# Pueden añadirse atributo...
# ¡¡EN TIEMPO DE EJECUCION!!

obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

'''
    La funcion toma un objeto cualquiera, busca en su interior atributos enteros
    con nombres que empiecen por "i", y los incrementa en uno.
'''

def incIntsI(obj):
    for clave in obj.__dict__.keys():
        if clave.startswith("i"):
            valor = getattr(obj, clave)
            if isinstance(valor, int):
                setattr(obj, clave, valor + 1)
                
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)