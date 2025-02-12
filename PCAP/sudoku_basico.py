
tablero = []
sudoku_OK = True

for i in range(9):  
    fila = input("Línea " + str(i + 1) + ": ")  
    if len(fila) == 9 and fila.isnumeric():  
        if sorted(fila) != list("123456789"):  
            print("La fila debe contener todos los números del 1 al 9")
            sudoku_OK = False
            break
        else:
            tablero.append(fila)
    else:
        print("La fila debe contener exactamente 9 números")
        sudoku_OK = False
        break

if sudoku_OK:
    print("El sudoku SÍ es válido")
else:
    print("El sudoku NO es válido")