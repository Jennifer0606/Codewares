"""
https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
"""


# My answer
def get_average(marks):
    return int(sum(marks) / len(marks))
#
# solution1
# def get_average(marks):
#     return sum(marks) // len(marks)
#
# solution2
# import math
#
#
# def get_average(marks):
#     return math.floor(sum(marks) // len(marks))
#
# Solution3
# import math
# import numpy
#
#
# def get_average(marks):
#     number = numpy.average(marks)
#     return math.floor(number)


print(get_average([2, 2, 2, 2]))  # should return 2
print(get_average([1, 5, 87, 45, 8, 8]))  # should return 25
print(get_average([2, 5, 13, 20, 16, 16, 10]))  # should return 11
print(get_average([1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]))  # should return 11
