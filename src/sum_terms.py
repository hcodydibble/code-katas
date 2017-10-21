"""Kata: Sum of the first nth term of Series - Returns the nth number
in a Series.

# 1 Best Practices solution by MMMAAANNN and others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Create and return the nth number in a Series."""
    x, j = 4, 1
    if n == 0:
        return "0.00"
    for i in range(n - 1):
        j = j + 1 / x
        x = x + 3
    return format(j, '.2f')
