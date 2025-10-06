# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attenmpt division 

        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both inputs must be numeric."