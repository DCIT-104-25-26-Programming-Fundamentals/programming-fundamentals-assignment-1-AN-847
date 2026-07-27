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

def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row = [float(x) for x in row_input.split()]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:g}" for val in row))

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

def add_matrices(mat_a, mat_b):
    rows = len(mat_a)
    cols = len(mat_a[0])
    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(mat_a[r][c] + mat_b[r][c])
        result.append(row)
    return result

def multiply_matrices(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])
    
    if cols_a != rows_b:
        print("Error: Columns of Matrix A must match Rows of Matrix B for multiplication.")
        return None
        
    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result

def main():
    print("--- PART A: Transpose a Matrix ---")
    matrix_a = read_matrix()
    print("\nOriginal Matrix:")
    print_matrix(matrix_a)
    print("Transposed Matrix:")
    print_matrix(transpose_matrix(matrix_a))
    
    print("\n--- PART B: Add Two Matrices ---")
    print("Enter Matrix A for addition:")
    mat_add1 = read_matrix()
    print("Enter Matrix B for addition (must be same size):")
    mat_add2 = read_matrix()
    
    if len(mat_add1) == len(mat_add2) and len(mat_add1[0]) == len(mat_add2[0]):
        print("Sum of Matrices:")
        print_matrix(add_matrices(mat_add1, mat_add2))
    else:
        print("Error: Matrices must have the exact same dimensions for addition.")

    print("\n--- PART C: Multiply Two Matrices ---")
    print("Enter Matrix A for multiplication:")
    mat_mul1 = read_matrix()
    print("Enter Matrix B for multiplication:")
    mat_mul2 = read_matrix()
    
    product = multiply_matrices(mat_mul1, mat_mul2)
    if product is not None:
        print("Product of Matrices (A x B):")
        print_matrix(product)

if __name__ == "__main__":
    main()