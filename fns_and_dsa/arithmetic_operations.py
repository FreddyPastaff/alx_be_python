def perform_operation(num1, num2, operation):
    operation = ("+", "-", "*", "/")
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 + num2
        case "*":
            return num1 * num2
        case "/":
            return "Error: Cannot divide by zero"
        case _:
            return "Invalid operation"


    





