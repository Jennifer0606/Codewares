"""
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
Introduction
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
"""

# My Solution
import math


def century(year):
    return math.ceil(year / 100)


# Best solution
# def century(year):
#     return (year + 99) // 100


print(century(1705))  # return 18
print(century(1900))  # return 19
print(century(1601))  # return 17
print(century(2000))  # return 20
print(century(356))  # return 4
print(century(89))  # return 1
