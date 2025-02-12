
while True:
    
    text1 = input("Introduce la 1ª palabra: ").upper()
    if not text1.isalpha():
        print("Error: "+text1+" no es una cadena alfabética.")
        break
    else:
        text2 = input("Introduce la 2ª palabra: ").upper()
        if not text2.isalpha():
            print("Error: "+text2+" no es una cadena alfabética.")
            break
    
    if sorted(text1) == sorted(text2):
        print("'"+text1+"' y '"+text2+"' son anagramas.")
    else:
        print("Las cadenas introducidas no son anagramas")
        
    input("\nPulsa Enter para continuar... [CTRL-C: Salir]\n")
            
    