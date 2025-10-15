def calculator(a, b, Operation):
    if Operation == "Add":
        return a + b
    elif Operation == "Subtract":
        return a - b
    elif Operation == "Multiply":
        return a * b
    elif Operation == "Divide":
        if b != 0: # Check to prevent division by zero
            return a / b
        else:
            return "Error: Division by zero, cannot divide by zero"
    else:
        return "Error: Invalid Operation"
    
# Example:
print(calculator(10, 5, "Add"))