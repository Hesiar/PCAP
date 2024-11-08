
#Cifrado Cesar

text = input("Ingresa tu mensaje: ")
cipher = ''

for char in text:
    if not char.isalpha():   #Si no es una cifra, pasa
        if char == ' ':
            cipher += ' '
            continue

    char = char.upper()   # m ---> M
    code = ord(char) + 1  # punto de codigo siguiente
    if code > ord('Z'):   # si rebasa el alfabeto...
        code = ord('A')    # ...vuelve al principio
    cipher += chr(code)   # convierte el punto de codigo a caracter
    
print(cipher)