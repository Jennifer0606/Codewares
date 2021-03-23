"""
https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
Implement a function which convert the given boolean value into its string representation.
"""


# my solution
# def boolean_to_string(b):
#     return "True" if b == True else "False"


# best solution
def boolean_to_string(b):
    return str(b)


print(boolean_to_string(True))  # return "True"
print(boolean_to_string(False))  # return "False"
