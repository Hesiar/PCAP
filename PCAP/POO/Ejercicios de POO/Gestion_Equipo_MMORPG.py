class InventarioLlenoError(Exception):
    pass

class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.rareza})"

class Personaje:
    MAX_ITEMS = 5  

    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_item(self, item):
        if len(self.inventario) >= Personaje.MAX_ITEMS:
            raise InventarioLlenoError(f"El inventario de {self.nombre} está lleno.\n ")
        else:
            self.inventario.append(item)
            print(f"{self.nombre} ha obtenido: {item}")
            print("")
        
    def eliminar_item(self, nombre_item):
        for item in self.inventario:
            if item.nombre == nombre_item:
                self.inventario.remove(item)
                print(f"{nombre_item} ha sido eliminado del inventario de {self.nombre}.")
                return
        print(f"{nombre_item} no se encontró en el inventario.")

    def mostrar_inventario(self):
        print(f"Mostrando inventario de {self.nombre}:")
        if not self.inventario:
            print(f"El inventario de {self.nombre} está vacío.")
        else:
            for item in self.inventario:
                print(f" - {item}")

try:
    guerrero = Personaje("Thorgrim")
    
    espada = Item("Espada de Fuego", "Arma", "Épico")
    escudo = Item("Escudo del Dragón", "Armadura", "Legendario")
    pocion = Item("Poción de Vida", "Consumible", "Común")
    arco = Item("Arco Largo", "Arma", "Raro")
    anillo = Item("Anillo de la Sabiduría", "Accesorio", "Épico")
    casco = Item("Casco de Hierro", "Armadura", "Común")

    guerrero.agregar_item(espada)
    guerrero.agregar_item(escudo)
    guerrero.agregar_item(pocion)
    guerrero.agregar_item(arco)
    guerrero.agregar_item(anillo)
    guerrero.agregar_item(casco)
    
    guerrero.mostrar_inventario()
    
except InventarioLlenoError as e:
    print(f"Error: {e}")

guerrero.eliminar_item("Poción de Vida")
guerrero.mostrar_inventario()
