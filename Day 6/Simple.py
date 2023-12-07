class Books:
    
    def __init__(self, name, pages): # constructor
        self.name = name
        self.pages = pages

    def print_book(self, author):
        print(self.name, self.pages, author)

# external object for class
book = Books("Maths", 50) # class constructor call
book.print_book("bala") # class method call

book1 = Books("Tamil", 100)
book1.print_book("krishnan")
