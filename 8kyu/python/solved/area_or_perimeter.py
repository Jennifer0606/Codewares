"""
https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

area_or_perimeter(6, 10) --> 32
area_or_perimeter(4, 4) --> 16
Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.
"""


# my solution
def area_or_perimeter(length, width):
    return length * width if length == width else 2 * (length + width)


print(area_or_perimeter(4, 4))  # return 16
print(area_or_perimeter(6, 10))  # return 32
