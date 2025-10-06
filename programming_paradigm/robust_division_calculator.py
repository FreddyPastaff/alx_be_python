# robust_division_calculator.py
def sef_divide(numerator, denominator):
    try:
        # convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attenmpt division 

        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."