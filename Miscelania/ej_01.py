import random

def generador_nombres():
    nombres = ["Juan", "Pedro", "Luis", "Carlos", "Mateo", "Fernando", "Javier", "Santiago", "Antonio", "Gonzalo"]
    random.shuffle(nombres) # Mezcla la lista de nombres aleatoriamente
    for nombre in nombres:
        yield nombre # devuelve un nombre cada vez que se llama
        
generador = generador_nombres()

for _ in range(10):
    print(next(generador)) # imprime 10 nombres aleatorios