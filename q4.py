def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Argument 's' must be a string.")

    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print("Scenario 1:")
print(string_reverse("Hello World"))
print()
print("Scenario 2:")
print(string_reverse("Python"))
