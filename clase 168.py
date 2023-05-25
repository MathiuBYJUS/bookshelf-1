
class Bookshelf:
    def __init__(self, libro, autor ,  año , lugar , costo , editorial):
        self.book_name=libro
        self.book_autor=autor
        self.year=año
        self.place=lugar
        self.book_price=costo
        self.book_edit=editorial
    
    def imprimir(self):
        print("Nombre del libro " + self.book_name)
        print("Autor del libro " + self.book_autor)
        print("Año de publicacion " + str(self.year))
        print("Lugar de publicacion " + self.place)
        print("Costo del libro " + str(self.book_price))
        print("Editorial " + self.book_edit)
        
    def years_since_published(self):
        Hace_cuantos_se_publico = 2023 - self.year
        print("Se publico hace " + str(Hace_cuantos_se_publico))
        
a=Bookshelf( "Las 48 leyes del poder" , "Robert Greene" , 1999 , "lugar" , 600 ,  "Espasa")
a.imprimir()
a.years_since_published()