fecha = ''

while True:
    fecha = input("Ingrese la fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric():
        break
    print("Debes introducir una fecha en formato AAAAMMDD.")
    
digito = 0
suma = 0

for c in fecha:
    suma += int(c)
    
if suma < 10:
    digito = suma
else:
    for c in str(suma):
        digito += int(c)
        
print("Tu dígito vital es:", digito)