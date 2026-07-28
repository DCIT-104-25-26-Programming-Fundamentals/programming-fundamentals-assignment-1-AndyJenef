# =============================================================================
def display_menu():
    """Displays the main menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_two_numbers():
    """Prompts the user for two numbers and returns them."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Returns (True, result) or (False, None) if b is zero."""
    if b == 0:
        return False, None
    return True, a / b


def modulus(a, b):
    """Returns (True, result) or (False, None) if b is zero."""
    if b == 0:
        return False, None
    return True, a % b


def exponent(base, exp):
    return base ** exp


if __name__ == "__main__":
    choice = None

    while choice != "7":
        display_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "1":
            a, b = get_two_numbers()
            print(f"Result: {a} + {b} = {add(a, b)}")

        elif choice == "2":
            a, b = get_two_numbers()
            print(f"Result: {a} - {b} = {subtract(a, b)}")

        elif choice == "3":
            a, b = get_two_numbers()
            print(f"Result: {a} * {b} = {multiply(a, b)}")

        elif choice == "4":
            a, b = get_two_numbers()
            success, result = divide(a, b)
            if success:
                print(f"Result: {a} / {b} = {result:.2f}")
            else:
                print("Error: Cannot divide by zero.")

        elif choice == "5":
            a, b = get_two_numbers()
            success, result = modulus(a, b)
            if success:
                print(f"Result: {a} % {b} = {result:.2f}")
            else:
                print("Error: Cannot perform modulus by zero.")

        elif choice == "6":
            a, b = get_two_numbers()
            print(f"Result: {a} ^ {b} = {exponent(a, b):.2f}")

        elif choice == "7":
            print("Goodbye!")

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        print()