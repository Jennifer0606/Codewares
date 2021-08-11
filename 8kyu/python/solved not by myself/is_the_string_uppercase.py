"""
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
Is the string uppercase?
Task
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
"""


# best solution
def is_uppercase(inp):
    return inp.isupper()


print(is_uppercase("c"))  # return False
print(is_uppercase("C"))  # return True
print(is_uppercase("hello I AM DONALD"))  # return False
print(is_uppercase("HELLO I AM DONALD"))  # return True
