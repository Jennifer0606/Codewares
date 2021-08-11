"""
https://www.codewars.com/kata/580a094553bd9ec5d800007d/train/python
"""


def apple(x):
    return "It's hotter than the sun!!" if pow(int(x), 2) > 1000 \
        else "Help yourself to a honeycomb Yorkie for the glovebox."


print(apple('50'))  # return "It's hotter than the sun!!"
print(apple(4))  # return "Help yourself to a honeycomb Yorkie for the glovebox."
print(apple("12"))  # return "Help yourself to a honeycomb Yorkie for the glovebox."
print(apple(60))  # return "It's hotter than the sun!!"
