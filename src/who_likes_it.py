"""Kata: Who likes it? - Return string of who likes 'it'.

# 1 Best Practices solution by zadoev and others

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
"""


def likes(names):
    """Take string of names and let you know who likes 'it'."""
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) > 3:
        return "{}, {} and {} others like this".format(names[0], names[1],
                                                       len(names) - 2)
    elif len(names) > 2:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    elif len(names) > 1:
        return "{} and {} like this".format(names[0], names[1])
