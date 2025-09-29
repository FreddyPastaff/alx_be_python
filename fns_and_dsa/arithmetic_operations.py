def perform_operation(num1, num2, operation,):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation")

    if operation == "int":
        return int(result)
    elif operation == "float":
        return float(result)
    elif operation == "str":
        return str(result)
    else:
        raise ValueError("Invalid result type")
    
    
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
