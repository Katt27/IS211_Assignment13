def fibonacci(n):
    """
    Recursively calculate the nth Fibonacci number.
    Args:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """
    Recursively calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of a and b.
    """
    # Base case
    if b == 0:
        return a
    # Recursive case
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """
    Recursively compare two strings lexicographically.
    Args:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    int: A negative number if s1 < s2, 0 if s1 == s2, and a positive number if s1 > s2.
    """
    # Base cases
    if not s1 and not s2:
        return 0
    elif not s1:
        return -ord(s2[0])
    elif not s2:
        return ord(s1[0])
    # Recursive case
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])

# Example function calls (comment these out before running in a production environment)
# print(fibonacci(10))  # Expected output: 55
# print(gcd(270, 192))  # Expected output: 6
# print(compareTo("apple", "apricot"))  # Expected output: Negative because "apple" < "apricot"
