#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int): First integer.
        b (int, optional): Second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
