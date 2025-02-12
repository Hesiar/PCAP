
class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
        
    def getSalario(self):
        return self.__salario
    
    #String de representacion del objeto
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.cargo} - {round(self.getSalario())}"

listaEmpleados = [
    Empleado("Juan", "Perez", "Gerente", 75000.0),
    Empleado("Ana", "Garcia", "Secretaria", 42000.0),
    Empleado("Pedro", "Lopez", "Programador", 63000.0),
    Empleado("Maria", "Rodriguez", "Contadora", 44000.0),
]

#Imprimir la lista de empleados
print("Lista de empleados:")
for empleado in listaEmpleados:
    print(empleado)

print("")
print("")
#Seleccionar los empleados cuyo slario sea > 50K al año
salario_anual = 50000.0
print("Lista de empleados VIP:")
for empleado in listaEmpleados:
    if empleado.getSalario() > salario_anual:
        print(empleado)
        



