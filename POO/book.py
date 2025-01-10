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
    

book1 = Book("Como craftear 1", 25, "Steve de Maincra", 12)
book2 = Book("Como craftear 2", 10, "Steve de Maincra", 12)
    