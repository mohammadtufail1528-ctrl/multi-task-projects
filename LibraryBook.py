
class Book():
    def __init__(self,title,Author,price):
        self.title=title
        self.Author=Author
        self.price=price
    def display(self):
            print(f"Book title:-{self.title}")
            print(f"Book Author_Name:-{self.Author}")
            print(f"Book Price:-{self.price}")
    def set_discount(self,discount):
           self.price =(100-discount)*self.price/100
            
    def get_discount(self):
        return self.price 

def run():
 print("3.Library project is runining.....")
 book=Book("Maskspoken","Kamlesh_Tirpadhi",1500)
 book.display()
 book.set_discount(5)
 print(book.get_discount())        
                
                
        