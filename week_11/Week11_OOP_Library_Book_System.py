class Book:

    def __init__(self, title,  author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def display_books(self):
        print(self.title)
        print(self.author)
        print(self.copies_available)

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print("book borrowed successfully")
        else:
            print("no copies available ")

    def return_book2(self):
        self.copies_available += 1
        print("book returned successfully")


book1 = Book("the big red dog", "author me", 0)

book2 = Book("cat in the hat", "author dan", 7)

book3 = Book("dan qthe man", "author sam", 0)

book1.display_books()
book1.borrow_book()
book1.display_books()
book1.return_book2()
book1.display_books()

'''
book2.display_books()
book2.borrow_book()
book2.return_book2()
book2.display_books()


book3.display_books()
book3.borrow_book()
book3.return_book2()
book3.display_books()
'''