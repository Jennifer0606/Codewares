"""
https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python
Given a string, write a function that returns the string with a question mark ("?") appends to the end,
unless the original string ends with a question mark, in which case, returns the original string.

ensure_question("Yes") == "Yes?"
ensure_question("No?") == "No?"
"""


# my solution
def ensure_question(s):
    while len(s) > 1:
        return s if s[-1] == "?" else s+"?"
    return "?"


# # best solution
# def ensure_question(s):
#     return s.rstrip('?') + '?'
#
#
# # other solution
# def ensure_question(s):
#     return s if s.endswith('?') else s + '?'


print(ensure_question(""))  # return "?"
print(ensure_question("Yes"))  # return "Yes?"
print(ensure_question("No?"))  # return "No?"
