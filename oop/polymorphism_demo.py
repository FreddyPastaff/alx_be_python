# polymorphism_demo.py

import math  # Importing math module to access the value of π (pi)

# Define the base class 'Shape'
class Shape:
    def area(self):
        """
        This method is meant to be overridden by subclasses.
        It raises an error if called directly from Shape.
        """
        raise NotImplementedError("Subclasses must implement the area method.")

# Define the 'Rectangle' subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

# Define the 'Circle' subclass
class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * self.radius ** 2