# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Basic Calculator is ready!")
    
    while True:
        operation = input("Choose an operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation in ('add', 'subtract', 'multiply', 'divide'):
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                
                if operation == 'add':
                    print(f"The result is: {add(a, b)}")
                elif operation == 'subtract':
                    print(f"The result is: {subtract(a, b)}")
                elif operation == 'multiply':
                    print(f"The result is: {multiply(a, b)}")
                elif operation == 'divide':
                    print(f"The result is: {divide(a, b)}")
            except ValueError:
                print("Please enter valid numbers.")
        else:
            print("Invalid operation. Please try again.")
