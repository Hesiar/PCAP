
class ExampleClass:
    def __init__(self, val = 1, val2 = 0):
        self.first = val
        self.foo = val2
        
    def set_second(self, val):
        self.second = val
         
ejemplo_objeto1 = ExampleClass()
ejemplo_objeto2 = ExampleClass(2, 3)
ejemplo_objeto2 = ExampleClass(10)

ejemplo_objeto3 = ExampleClass(3)

ejemplo_objeto3.third = 5

print(ejemplo_objeto1.__dict__)
print(ejemplo_objeto2.__dict__)
print(ejemplo_objeto3.__dict__)
