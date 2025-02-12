
palabra = input("Introduce la palabra a buscar: ").upper()
grupo = input("Introduce un grupo de caracteres: ").upper()

contiene = True
inicio= 0

for c in palabra:
    posicion = grupo.find(c)
    if posicion == -1:
        contiene = False
        break
    inicio = posicion +1
    
if (contiene):
    print("La palabra '", palabra, "' se ha encontrado en el grupo de caracteres otorgado.")
else:
    print("La palabra '", palabra, "' no se ha encontrado en el grupo de caracteres otorgado.")
        
    