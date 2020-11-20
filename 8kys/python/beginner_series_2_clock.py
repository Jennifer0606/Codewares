"""
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

Example:
past(0, 1, 1) == 61000
"""


# my answer
def past(h, m, s):
    h = h * 60 * 60
    m = m * 60
    return (h + m + s) * 1000


# Best Practice
# def past(h, m, s):
#     return (3600 * h + 60 * m + s) * 1000


print(past(0, 1, 1))  # return 61000
print(past(1, 1, 1))  # return 3661000
print(past(0, 0, 0))  # return 0
print(past(1, 0, 1))  # return 3601000
print(past(1, 0, 0))  # return 3600000
