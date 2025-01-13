
class ExampleClass:
    def __init__(self, val):
        self.a = 0
        self.b = 0
        if val % 2 != 0:
            self.a = val
        else:
            self.b = 1
            
example_object = ExampleClass(12)
example_object2 = ExampleClass(11)

try:
    print(example_object.a)
    print(example_object.b)
    print()
    print(example_object2.a)
    print(example_object2.b)
except AttributeError:
    print("Error: unable to print attributes")