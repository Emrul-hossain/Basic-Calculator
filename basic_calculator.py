def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check for division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    # Check for division by zero
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


# Display menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

# Take user input for operation choice
choice = input("Enter choice (1/2/3/4/5): ")

try:
    # Take user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform selected operation
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == '5':
        result = modulus(num1, num2)
        print(f"{num1} % {num2} = {result}")
    else:
        print("Invalid input! Please choose between 1 to 5.")

# Handle non-numeric input errors
except ValueError:
    print("Error: Please enter valid numbers.")