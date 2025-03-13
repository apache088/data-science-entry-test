def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float, complex)) and isinstance(y, (int, float, complex))):
        return -1

    x, y = y, x
    return f"Swapped values: x={x}, y={y}"


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
print("Scenario 1:")
print(swap("Apple", 10))
print()
print("Scenario 2:")
print(swap(9, 17))
