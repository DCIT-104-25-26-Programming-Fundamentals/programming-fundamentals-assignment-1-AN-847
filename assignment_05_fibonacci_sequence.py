# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms():
    """PART A - Print the First N Terms"""
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    # Using a loop to generate the sequence
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(str(a))
        a, b = b, a + b
        
    print(f"Fibonacci sequence: {' '.join(sequence)}")


def check_fibonacci_number():
    """PART B - Check if a Number Belongs to the Sequence"""
    try:
        num = int(input("\nEnter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Using a loop to generate Fibonacci numbers until we reach or exceed the target number
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
        
    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


# Execute the functions
if __name__ == "__main__":
    print_fibonacci_terms()
    check_fibonacci_number()
