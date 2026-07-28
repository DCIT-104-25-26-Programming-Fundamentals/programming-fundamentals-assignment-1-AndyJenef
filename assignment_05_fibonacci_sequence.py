# =============================================================================
def print_fibonacci(n):
    """Prints the first n terms of the Fibonacci sequence on one line."""
    a, b = 0, 1
    terms = []

    for _ in range(n):
        terms.append(str(a))
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(terms))


def is_fibonacci(num):
    """Returns True if num appears in the Fibonacci sequence, False otherwise."""
    if num < 0:
        return False

    a, b = 0, 1

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


if __name__ == "__main__":
    # -------------------------------------------------------------------
    # PART A — Print the First N Terms
    # -------------------------------------------------------------------
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
    else:
        print_fibonacci(n)

    # -------------------------------------------------------------------
    # PART B — Check if a Number Belongs to the Sequence
    # -------------------------------------------------------------------
    num = int(input("\nEnter a number to check: "))

    if is_fibonacci(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")