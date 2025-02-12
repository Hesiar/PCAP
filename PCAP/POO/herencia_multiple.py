
class Humano:
    
    planeta = "Tierra"
    
    def __init__(self, nombre):
        self.nombre = nombre
        
class Saiyan:
    
    planeta = "Sadala"
    
    def __init__(self, nombre):
        self.nombre = nombre
        
class Mestizo(Saiyan, Humano):
    def __init__(self, nombre, madre, padre):
        self.nombre = nombre
        self.madre = madre.nombre
        self.padre = padre.nombre
    
    def verAncestros(self):
        for ancestro in Mestizo.__bases__:
            print(ancestro.__name__, end=' ')
        print()

goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegeta")
bulma = Humano("Bulma")
trunks = Mestizo("Trunks", bulma, vegeta)

print(trunks.nombre," tiene como padres a ", trunks.madre, " y ", trunks.padre)
print()
# Imprime el nombre de la clase
print("Nombre de la clase de la varibale 'goku':")
print(type(goku).__name__)
print()
# Imprime los atributos y métodos del objeto
print("Atributos y métodos de la variable 'trunks':")
print(trunks.__dict__)
print(trunks.__module__) # Imprime el módulo donde se encuentra la clase
print(f"El padre de {trunks.nombre} es {trunks.__dict__["padre"]} y su madre es {trunks.__dict__['madre']}.")
print()

# trunks.verAncestros()

print(trunks.planeta)
trunks.planeta = "Tierra"
print()
print(f"Trunks es de la {trunks.planeta}")
print(f"Goku es de {goku.planeta}")
print()

if type(trunks).__name__ == "Mestizo":
    if issubclass(Mestizo, Saiyan):
        print(f"{trunks.nombre} puede convertirse en super saiyan")
        if issubclass(Mestizo, Humano):
            print(f"{trunks.nombre} tiene una madre humana.")
    else:
        print(f"{trunks.nombre} no puede convertirse en super saiyan")