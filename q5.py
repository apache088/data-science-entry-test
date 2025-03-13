def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float, complex)) and isinstance(divisor, (int, float, complex))):
        raise TypeError("Arguments 'num' and 'divisor' must be numeric.")

    if divisor == 0:
        raise ValueError("Argument 'divisor' cannot be zero.")

    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print("Scenario 1:")
print(check_divisibility(10, 2))
print()
print("Scenario 2:")
print(check_divisibility(7, 3))
