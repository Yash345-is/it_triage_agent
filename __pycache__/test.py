class Book:

    def __init__(self,title,author):

        self.title = title
        self.author = author
        self.is_borrowed = "False"
        

    def show(self):    

        print("Title:",self.title,"Author:",self.author)

        

    def borrow(self):
        self.is_borrowed = "True"
        print(self.is_borrowed)

    def return_book(self):
        self.is_borrowed = "False"
        print(self.is_borrowed)

b1 = Book("Percy Jackson","Rick Riordan")

b1.show()

b1.borrow()

print("Book returned")

b1.return_book()

b2 = Book("Dog Man","Dav Pilkey")

b2.show()

b2.borrow()

print("Book returned")

b2.return_book()

b3 = Book("The Trials Of Apollo","Rick Riordan")

b3.show()      

b3.borrow()

print("Book returned")

b3.return_book()