"""
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
Write a function called repeat_str which repeats the given string src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
"""


def repeat_str(repeat, string):
    return repeat * string


print(repeat_str(4, 'a'))  # return "aaaa"
print(repeat_str(3, 'hello '))  # return 'hello hello hello '
print(repeat_str(2, 'abc'))  # return 'abcabc'
