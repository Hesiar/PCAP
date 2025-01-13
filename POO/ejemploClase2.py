
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
        
objeto_1 = ExampleClass()
objeto_2 = ExampleClass(2)
objeto_3 = ExampleClass(4)

print(objeto_1.__dict__, objeto_1.counter)
print(objeto_2.__dict__, objeto_2.counter)
print(objeto_3.__dict__, objeto_3.counter)
