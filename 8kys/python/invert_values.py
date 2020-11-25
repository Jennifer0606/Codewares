"""
https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
"""


# my solution
def invert(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] < 0:
            new_lst.append(abs(lst[i]))
        else:
            new_lst.append(-lst[i])
    return new_lst


# best solution
# def invert(lst):
#     return [-x for x in lst]

print(invert([1, 2, 3, 4, 5]))  # return [-1,-2,-3,-4,-5]
print(invert([1, -2, 3, -4, 5]))  # return [-1,2,-3,4,-5]
print(invert([]))  # return []
