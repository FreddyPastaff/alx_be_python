class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__available = True

    def check_out(self):
        self.__available = False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available

    def __str__(self):
        return f"{self.__title} by {self.__author}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Book) and self.__title == other.__title and self.__author == other.__author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books = [b for b in self.books if b != book]

    def list_available_books(self):
        return [book for book in self.books if book.is_available()]

    def check_out_book(self, book):
        for b in self.books:
            if b == book and b.is_available():
                b.check_out()
                break

    def return_book(self, book):
        for b in self.books:
            if b == book and not b.is_available():
                b.return_book()
                break
