class Book:
    def __init__(self, titulo, cantidad, autor, precio):
        self.titulo=titulo
        self.cantidad=cantidad
        self.autor=autor
        self.__precio=precio
        self.__descuento=None
    
    def set_descuento(self, descuento):
        self.__descuento=descuento
    
    def get_precio(self):
        if self.__descuento:
            return self.__precio * (1-self.__descuento)
        return self.__precio
    
    def __repr__(self):
        return "Titulo: "+self.titulo+" Cantidad: "+self.cantidad+" Autor: "+self.autor+" Precio: "+round(self.get_precio(),3)+" €"

class Novel(Book):
    def __init__(self, titulo, cantidad, autor, precio, paginas):
        super().__init__(titulo, cantidad, autor, precio)
        self.paginas = paginas

class Academica(Book):
    def __init__(self, titulo, cantidad, autor, precio, rama):
        super().__init__(titulo, cantidad, autor, precio)
        self.rama = rama
    def __repr__(self):
        def __repr__(self):
            return "Titulo: "+self.titulo+" Genero: "+self.rama+" Cantidad: "+self.cantidad+" Autor: "+self.autor+" Precio: "+round(self.get_precio(),3)+" €"
    
novela1 = Novel("La comunidad del anillo", 30, "J.R.R Tolkien", 30, 560)
novela1.set_descuento(0.20)

ensayo1 = Academica("Modernidad Liquida",12, "Z.Bauman", 18, "Sociologia")

print(novela1)
print(ensayo1)