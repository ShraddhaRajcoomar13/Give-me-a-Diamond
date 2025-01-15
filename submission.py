def diamond(n):
    # Return None if n is even or negative
    if n <= 0 or n % 2 == 0:
        return None

    # Build the diamond
    result = []
    for i in range(n):
        # Calculate the number of stars for this row
        stars = n - abs(n - 2 * i - 1)  # Symmetric star calculation
        spaces = (n - stars) // 2  # Center alignment
        result.append(" " * spaces + "*" * stars)

    # Join the rows with newline characters
    return "\n".join(result) + "\n"
