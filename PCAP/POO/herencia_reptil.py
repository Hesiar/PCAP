class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Serpiente(Reptil):
    pass
    
class Culebra(Serpiente):
    pass

reptil = Reptil("Lagarto")
reptil2 = Serpiente("Mamba negra")
reptil3 = Culebra("Culebra iberica")

print(type(reptil).__name__) 
print(type(reptil2).__name__)
print(type(reptil3).__name__) 
print()

for cls1 in [Reptil, Serpiente, Culebra]:
    for cls2 in [Reptil, Serpiente, Culebra]:
        print(issubclass(cls1, cls2), end="\t")
    print()
    
print()
print(f"\t\t{Reptil.__name__}\t{Serpiente.__name__} {Culebra.__name__}") 
  
for cls1 in [Reptil, Serpiente, Culebra]:
    print(cls1.__name__, end="  \t")
    for cls2 in [Reptil, Serpiente, Culebra]:
        print(issubclass(cls1, cls2), end="\t")
    print()
print()

print("---------------------------------------------------------------------------------------")
print()

print(f"\t\t{type(reptil).__name__}\t\t{type(reptil2).__name__}\t{type(reptil3).__name__}")

for cls1 in [type(reptil), type(reptil2), type(reptil3)]:
    print(cls1.__name__, end="  \t")
    for cls2 in [type(reptil), type(reptil2), type(reptil3)]:
        print(issubclass(cls1, cls2), end="\t\t")
    print()

print("---------------------------------------------------------------------------------------")
print()

reptil = Reptil("Rana")
reptil2 = Serpiente("Vibora")
reptil3 = Culebra("Cocodrilo")

reptil = reptil2
#reptil2 = reptil3

print(reptil == reptil2, reptil is reptil2)
print(reptil2 == reptil3, reptil2 is reptil3)
