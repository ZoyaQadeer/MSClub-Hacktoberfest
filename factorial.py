# factorial.py

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

