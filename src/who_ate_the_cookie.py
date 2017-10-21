"""Kata: Who ate the cookie? - Return a different string based on input.

# 1 Best Practices solution by acaccia and others

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica",
            int:"Monica"}.get(type(x), "the dog")
"""


def cookie(x):
    """Check the type of x and return different string."""
    if type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) is int or float:
        return "Who ate the last cookie? It was Monica!"
