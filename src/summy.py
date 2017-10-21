"""Kata: Summy - Return sum of a string of integers.

# 1 Best Practices solution by fenring76 and others

def summy(string_of_ints):
    return sum(map(int,string_of_ints.split()))
"""


def summy(string_of_ints):
    """Take a string of integers and return their sum."""
    answer = 0
    for number in string_of_ints.split(" "):
        answer += int(number)
    return answer
