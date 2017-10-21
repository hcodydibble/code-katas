"""Kata:Selective Array Reversing - Return an array with the numbers reversed in
    groups based on the number passed in as the l parameter.

# 1 Best Practices solution by Blind4Basics

def sel_reverse(arr,l):
    return [ elt for i in range(0, len(arr), l) for elt in arr[i:i+l][::-1] ] if l != 0 else arr
"""


# def sel_reverse(arr, l):
#     """First attempt."""
#     import copy
#     if l == 0:
#         return arr
#     if l > len(arr):
#         return arr[::-1]
#     new_list = copy.deepcopy(arr)
#     fill_list = []
#     breaker = l
#     while breaker > -20:
#             fill_list.append(new_list[0:l][::-1])
#             del new_list[0:l]
#             breaker -= 1
#     return sum(fill_list, [])


# def sel_reverse(arr, l):
#     """Second attempt."""
#     if l == 0:
#         return arr
#     answer = []
#     for i in range(0, len(arr), l):
#         answer.append(arr[i:i + l][::-1])
#     return sum(answer, [])


def sel_reverse(arr, l):
    """Return a list with items reversed in steps."""
    if l == 0:
        return arr
    arr = [arr[i:i + l][::-1] for i in range(0, len(arr), l)]
    return sum(arr, [])
