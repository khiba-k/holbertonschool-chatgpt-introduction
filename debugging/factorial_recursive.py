#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given integer.

    Parameters:
    - n (int): The integer for which factorial is to be calculated.

    Returns:
    - int: The factorial of the given integer.

    Raises:
    - ValueError: If the input is not a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <integer>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = factorial(number)
        print(result)
    except ValueError as e:
        print("Error:", e)

