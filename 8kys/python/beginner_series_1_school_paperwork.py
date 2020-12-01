"""
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
Your classmates asked you to copy some paperwork for them.
You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.

Example:
paperwork(5, 5) == 25
Note: if n < 0 or m < 0 return 0!
"""


# my solution
def paperwork(n, m):
    while n < 0 or m < 0:
        return 0
    return n * m


# best solution
# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0


print(paperwork(5, 5))  # return 25
