"""Kata: Sum of two lowest positive integers - Returns the sum of two lowest 
positive integers in a list.

# 1 Best Practices solution by danman1979 and others

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Find two lowest positive integers and add them."""
    return sorted(numbers)[0] + sorted(numbers)[1]
