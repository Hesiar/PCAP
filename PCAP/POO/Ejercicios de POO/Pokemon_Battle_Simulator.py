class Pokemon:
    ventajas = {
        "Agua": "Fuego",
        "Fuego": "Planta",
        "Planta": "Agua",
        "Eléctrico": "Agua"
    }

    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque

    def atacar(self, otro_pokemon):
        if otro_pokemon.vida <= 0:
            raise ValueError(f"{otro_pokemon.nombre} ya ha sido derrotado.")
        
        daño = self.ataque
        ventaja = Pokemon.ventajas.get(self.tipo) == otro_pokemon.tipo

        if ventaja:
            mensaje = f"¡Atención! {self.nombre} es de tipo {self.tipo}, por lo que causa daño aumentado a {otro_pokemon.nombre}, que es de tipo {otro_pokemon.tipo}."
            print(mensaje)
            daño *= 1.5 

        otro_pokemon.vida -= daño
        if otro_pokemon.vida <= 0:
            otro_pokemon.vida = 0

        print(f"{self.nombre} ataca a {otro_pokemon.nombre} causando {daño} de daño.")
        print(f"{otro_pokemon.nombre} tiene {otro_pokemon.vida} puntos de vida restantes.\n")
        
        if otro_pokemon.vida == 0:
            print(f"{otro_pokemon.nombre} ha sido derrotado.")

pikachu = Pokemon("Pikachu", "Eléctrico", 100, 20)
charizard = Pokemon("Charizard", "Fuego", 120, 25)
blastoise = Pokemon("Blastoise", "Agua", 150, 22)
bulbasaur = Pokemon("Bulbasaur", "Planta", 90, 18)

try:
    blastoise.atacar(charizard)  
    charizard.atacar(blastoise)
    blastoise.atacar(charizard)
    charizard.atacar(blastoise)
    blastoise.atacar(charizard)
    charizard.atacar(blastoise)
    blastoise.atacar(charizard)
except ValueError as e:
    print(e)
