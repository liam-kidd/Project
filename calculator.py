# calculator.py

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    """Runs the text-based calculator."""
    print("Welcome to the Text-Based Calculator!")
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        try:
            # Get user input for operation choice
            choice = input("Enter the number of the operation (1/2/3/4) or 'q' to quit: ").lower()

            if choice == 'q':
                print("Goodbye!")
                break

            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please choose a valid option.")
                continue

            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter valid numbers only.")

if __name__ == "__main__":
    calculator()
# new change
