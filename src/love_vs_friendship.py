"""Kata: Love vs Friendship - Return total sum of a string.

# 1 Best Practices solution by anter69 and others

def words_to_marks(s):
    return sum(ord(c)-96 for c in s)
"""


def words_to_marks(s):
    """Add a strings value up and return the total."""
    val_dict = {'l': 12, 'o': 15, 'd': 4, 'm': 13, 'y': 25, 'j': 10, 'v': 22,
                'r': 18, 'p': 16, 't': 20, 'i': 9, 'u': 21, 'c': 3, 'g': 7,
                'b': 2, 'k': 11, 'w': 23, 'x': 24, 'e': 5, 'z': 26, 'h': 8,
                's': 19, 'q': 17, 'f': 6, 'n': 14, 'a': 1}
    answer = 0
    for letter in s:
        answer += val_dict[letter]
    return answer
