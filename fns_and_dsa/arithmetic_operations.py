def perform_operation(num1, num2, operation, result_type):
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

    if result_type == "int":
        return int(result)
    elif result_type == "float":
        return float(result)
    elif result_type == "str":
        return str(result)
    else:
        raise ValueError("Invalid result type")
    
    
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
