"""
https://www.codewars.com/kata/57a386117cb1f31890000039/train/python
Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.
"""


# my solution
def parse_float(string):
    try:
        return float(string)
    except:
        return None


print(parse_float("1.0"))  # return 1.0
print(parse_float("a"))  # return None
print(parse_float("234.0234"))  # return 234.0234
