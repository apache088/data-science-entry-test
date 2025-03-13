def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        raise TypeError("Argument 'lst' must be a list.")

    index = 0
    while index < len(lst):
        current_item = lst[index]

        if not isinstance(current_item, (int, float, complex)):
            raise TypeError("Items in argument 'lst' must be numeric.")

        if current_item < 0:
            return current_item

        index += 1

    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
print("Scenario 1:")
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print()
print("Scenario 2:")
print(find_first_negative([2, 10, 7, 0]))
