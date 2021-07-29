"""
https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""


# my solution
def bool_to_word(boolean):
    return 'Yes' if boolean is True else "No"


# best solution
def bool_to_word(bool):
    return "Yes" if bool else "No"


print(bool_to_word(True))  # 'Yes'
print(bool_to_word(False))  # 'No'
