# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    """Reads a rows x cols matrix, one row per line, space-separated values."""
    matrix = []
    for i in range(rows):
        while True:
            values = input(f"Enter row {i + 1}: ").split()
            if len(values) != cols:
                print(f"Error: Expected {cols} values, got {len(values)}. Try again.")
                continue
            matrix.append([int(v) for v in values])
            break
    return matrix


def print_matrix(matrix):
    """Prints a matrix in a neat, aligned grid."""
    for row in matrix:
        print(" ".join(f"{val:5}" for val in row))


def transpose_matrix(matrix, rows, cols):
    """Returns the transpose of a rows x cols matrix."""
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b, rows, cols):
    """Returns the element-wise sum of two rows x cols matrices."""
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b, m, n, p):
    """Multiplies an m x n matrix A by an n x p matrix B, returning an m x p result."""
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":
    # -----------------------------------------------------------------------
    # PART A — Transpose
    # -----------------------------------------------------------------------
    print("===== PART A: Transpose a Matrix =====")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix, rows, cols)

    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # -----------------------------------------------------------------------
    # PART B — Addition
    # -----------------------------------------------------------------------
    print("\n===== PART B: Add Two Matrices =====")
    add_rows = int(input("Enter number of rows: "))
    add_cols = int(input("Enter number of columns: "))

    print("\nEnter Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols)

    print("\nEnter Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols)

    sum_result = add_matrices(matrix_a, matrix_b, add_rows, add_cols)

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)
    print("\nSum (A + B):")
    print_matrix(sum_result)

    # -----------------------------------------------------------------------
    # PART C — Multiplication
    # -----------------------------------------------------------------------
    print("\n===== PART C: Multiply Two Matrices =====")
    m = int(input("Enter rows of Matrix A (M): "))
    n = int(input("Enter columns of Matrix A (N): "))

    print("\nEnter Matrix A:")
    mat_a = read_matrix(m, n)

    n2 = int(input(f"\nEnter rows of Matrix B (must equal N = {n}): "))
    p = int(input("Enter columns of Matrix B (P): "))

    if n2 != n:
        print("Error: Number of columns in A must equal number of rows in B.")
    else:
        print("\nEnter Matrix B:")
        mat_b = read_matrix(n2, p)

        product = multiply_matrices(mat_a, mat_b, m, n, p)

        print("\nMatrix A:")
        print_matrix(mat_a)
        print("\nMatrix B:")
        print_matrix(mat_b)
        print("\nProduct (A x B):")
        print_matrix(product)