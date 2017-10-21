"""Kata: Stop gninnipS My sdroW! - Return a string with every word equal to or
    greater than five reversed.

# 1 Best Practices solution by medve and others

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
"""


def spin_words(sentence):
    """Take a string and reverse all words 5+ characters."""
    answer_array = []
    split = sentence.split(" ")
    for word in split:
        if len(word) < 5:
            answer_array.append(word)
        else:
            answer_array.append(word[::-1])
    return " ".join(answer_array)
