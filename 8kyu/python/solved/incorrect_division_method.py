"""
https://www.codewars.com/kata/54d1c59aba326343c80000e7/train/python
This method, which is supposed to return the result of dividing its first argument by its second, isn't always returning correct values. Fix it.
"""


def divide_numbers(x, y):
    return x / y


print(divide_numbers(4, 2))  # return 2
print(divide_numbers(10, 2))  # return 5
print(divide_numbers(9, 4))  # return 2.25
print(divide_numbers(21, 5))  # return 4.2
print(divide_numbers(9, 3))  # return 3
print(divide_numbers(1, 100))  # return 0.01
