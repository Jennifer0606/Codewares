"""
https://www.codewars.com/kata/55d8618adfda93c89600012e/train/python
What could be easier than comparing integer numbers? However,
the given piece of code doesn't recognize some of the special numbers for a reason to be found.
Your task is to find the bug and eliminate it.
"""


def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


print(what_is(0))  # return "nothing"
print(what_is(123))  # return "nothing"
print(what_is(-1))  # return "nothing"
print(what_is(42))  # return "everything"
print(what_is(42 * 42))  # return "everything squared"
