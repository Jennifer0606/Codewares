"""
https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

# best solution
# from functools import reduce
#
#
# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)


# other solution
def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product


grow([1, 2, 3])  # return 6
grow([4, 1, 1, 1, 4])  # return 16
grow([2, 2, 2, 2, 2, 2])  # return 64
