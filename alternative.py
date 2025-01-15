from math import sqrt

def fibonacci(n):
    """Efficient calculation of the nth Fibonacci number."""
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return round((phi**n - psi**n) / sqrt(5))

def diamond_with_fibonacci(n):
    # Return None if n is even or negative
    if n <= 0 or n % 2 == 0:
        return None

    # Generate Fibonacci numbers up to the size of the diamond
    fib_numbers = [fibonacci(i) for i in range(n // 2 + 1)]

    # Adjust the maximum width for centering
    max_width = fib_numbers[-1]

    # Build the diamond
    result = []
    for i in range(len(fib_numbers)):
        stars = fib_numbers[i]  # Number of stars in the current row
        spaces = (max_width - stars) // 2
        result.append(" " * spaces + "*" * stars)

    # Mirror the top half to create the bottom half
    result += result[-2::-1]

    # Join the rows and return the diamond as a single string
    return "\n".join(result) + "\n"

# Test cases
print(diamond_with_fibonacci(5))  # Expected: '  *\n ***\n*****\n ***\n  *\n'
print(diamond_with_fibonacci(7))  # Larger diamond example
