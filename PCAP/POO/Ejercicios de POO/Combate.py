class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ya ha sido derrotado.")
            return

        objetivo.vida -= self.ataque
        if objetivo.vida < 0:
            objetivo.vida = 0
            print(f"{objetivo.nombre} ya ha sido derrotado.\n")
        else:
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {self.ataque} de daño.")
            print(f"{objetivo.nombre} tiene {objetivo.vida} puntos de vida restantes.\n")
            if objetivo.vida <= 0:
                print(f"{objetivo.nombre} ha sido derrotado.\n")
                return

    def mostrar_estadisticas(self):
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}")

class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, magia):
        super().__init__(nombre, vida, ataque)
        self.magia = magia

    def lanzar_hechizo(self, objetivo):
        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ya ha sido derrotado.")
            return

        daño_magico = self.ataque + self.magia
        objetivo.vida -= daño_magico
        if objetivo.vida < 0:
            objetivo.vida = 0
            print(f"{objetivo.nombre} ha sido derrotado.\n")
        else:
            print(f"{self.nombre} lanza un hechizo a {objetivo.nombre} causando {daño_magico} de daño.")
            print(f"{objetivo.nombre} tiene {objetivo.vida} puntos de vida restantes.\n")
            if objetivo.vida <= 0:
                print(f"{objetivo.nombre} ha sido derrotado.\n")
                return

    def mostrar_estadisticas(self):
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Magia: {self.magia}")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, armadura):
        super().__init__(nombre, vida, ataque)
        self.armadura = armadura

    def recibir_golpe(self, daño):
        daño_final = max(daño - self.armadura, 0)
        self.vida -= daño_final
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {daño_final} de daño tras bloquear con su armadura.")
        print(f"{self.nombre} tiene {self.vida} puntos de vida restantes.\n")

    def mostrar_estadisticas(self):
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Armadura: {self.armadura}")

class Enemigo:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ya ha sido derrotado.")
            return
        
        if isinstance(objetivo, Guerrero):
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {self.ataque} de daño.")
            print(f"Pero su ataque es bloqueado por la armadura de {objetivo.nombre}.")
            objetivo.recibir_golpe(self.ataque)
        else:
            objetivo.vida -= self.ataque
            if objetivo.vida < 0:
                objetivo.vida = 0
                print(f"{objetivo.nombre} ha sido derrotado.")
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {self.ataque} de daño.")
            print(f"{objetivo.nombre} tiene {objetivo.vida} puntos de vida restantes.\n")

    def mostrar_estadisticas(self):
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}")


print("\n--- ESTADÍSTICAS DE LOS PERSONAJES ---\n")
mago = Mago("Merlín", 80, 10, 25)
guerrero = Guerrero("Thorin", 120, 15, 10)
orco = Enemigo("Orco Salvaje", 100, 12)

mago.mostrar_estadisticas()
guerrero.mostrar_estadisticas()
orco.mostrar_estadisticas()

print("\n--- COMBATE ---\n")
mago.lanzar_hechizo(orco)
orco.atacar(guerrero)
guerrero.atacar(orco)
orco.atacar(mago)
mago.lanzar_hechizo(orco)
orco.atacar(mago)
guerrero.atacar(orco)

print("\n--- ESTADÍSTICAS FINALES ---\n")
mago.mostrar_estadisticas()
guerrero.mostrar_estadisticas()
orco.mostrar_estadisticas()
