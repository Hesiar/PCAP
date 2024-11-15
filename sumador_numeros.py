
# Sumador de Numeros

from imprime_pares import imprime_pares as impp

'''
    Este programa toma una serie de numeros como entrada,
    y devuelve la suma total.
    Si encuentra caracteres no numericos, lanza una excepcion
'''

line = input("Ingrese una serie de numeros separados por espacios: ")
strings = line.split()
total = 0
try:
    for substring in strings:
        total += float(substring)
    print("La suma total es: ", total)
except:
    print("Error: '"+substring+"' no es un numero.")


impp(strings)