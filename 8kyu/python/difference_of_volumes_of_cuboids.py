"""
https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
In this simple exercise, you will create a program that will take two lists of integers, a and b.
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b.
You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20.
Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.
"""


# my solution
def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])


# best solution
from numpy import prod


def find_difference(a, b):
    return abs(prod(a) - prod(b))


print(find_difference([3, 2, 5], [1, 4, 4]))  # return 14
print(find_difference([9, 7, 2], [5, 2, 2]))  # return 106
