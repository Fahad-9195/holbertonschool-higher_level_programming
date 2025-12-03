#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It ensures that the inputs are integers or floats.
Float values are casted to integers before addition.
A TypeError is raised if the inputs are invalid.
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Both values must be integers or floats, otherwise
    a TypeError is raised.

    Returns:
        int: the integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
