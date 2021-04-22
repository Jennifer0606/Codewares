"""
https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


# my solution
def find_average(numbers):
    return sum(numbers) / len(numbers)


# best solution
def find_average(array):
    return sum(array) / len(array) if array else 0


print(find_average([1, 2, 3]))  # return 2
