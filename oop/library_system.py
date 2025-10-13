# Base class for all books
class Book:
    def __init__(self, title, author,):
        # Common attributes for any book
        self.title = title
        self.author = author

    def __str__(self):
        # String representation of the book
        return f"Title: {self.title}, Author: {self.author}"
    
# Derived Class - EBook

class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initialize base class attributes

        super().__init__(title, author)
        # Add file_size specific to EBook
        self.file_size = file_size
    
    def __str__(self):
        return super().__str__() + f", File Size: {self.file_size}KB"

# Derived Class - PrintBook

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initialize base class attributes

        super().__init__(title, author)
        # Add page_count specific to PrintBook

        self.page_count = page_count
    def __str__(self):
        return super().__str__() + f", Page Count: {self.page_count}"
    
# Compostion - Library

class Library:
    def __init__(self):
        #Initialize an empty list to store books
        self.books = []
    def add_book(self, book):
        # Add a book to the library

        self.books.append(book)
    
    def list_books(self):
        # Print details of each book
        
        for book in self.books:
            print(book)