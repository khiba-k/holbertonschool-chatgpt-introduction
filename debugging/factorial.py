import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Check if the user provides a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py <number>")
    sys.exit(1)

# Try to convert the command-line argument to an integer
try:
    number = int(sys.argv[1])
except ValueError:
    print("Error: Please provide an integer as input.")
    sys.exit(1)

# Check if the number is non-negative
if number < 0:
    print("Error: Please provide a non-negative integer.")
    sys.exit(1)

# Calculate and print the factorial
f = factorial(number)
print(f)

