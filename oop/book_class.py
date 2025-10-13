# Define the Book class
class Book:
    # Constructor method: called when a new Book is created
    def __init__(self, title, author, year):
        """Initializes a Book instance with title, author, and publication year.
        parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year
    
    # Destructor method: called when the object is deleted

    def __del__(self):
        """Prints a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

# user-friendly string representation
    def __str__(self):
        """Returns a readable string describing the book.
    Example: 1984 by George Orwell, published in 1949"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
# Official representation: useful for debugging or recreating the object

    def __repr__(self):
        """Returns a string that could be used to recreate the Book object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

