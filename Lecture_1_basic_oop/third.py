class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
my_book = Book("My Book2", "again me", 5)
print(my_book.name)
book_3 = Book("My Book", "Me", 200)
print(id(book))
print(id(book_3))

print(type(5))
a = int("5")


