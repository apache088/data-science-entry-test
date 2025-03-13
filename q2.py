def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        raise TypeError("Argument 'lst' must be a list.")

    return [replace_val if item == find_val else item for item in lst]


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
print("Scenario 1:")
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print()
print("Scenario 2:")
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
