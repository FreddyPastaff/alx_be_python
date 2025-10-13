# class_static_methods_demo.py

class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: performs addition.
        Does NOT access class or instance data.
        Ideal for utility-style operations.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: performs multiplication.
        Has access to the class via 'cls'.
        Can use or modify class-level attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b