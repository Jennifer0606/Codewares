"""
https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

Write function that checks if a given string (case insensitive) is a palindrome.
"""


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


print(is_palindrome('a'))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('Abba'))  # True
print(is_palindrome('malam'))  # True
print(is_palindrome('walter'))  # False
print(is_palindrome('kodok'))  # True
print(is_palindrome('Kasue'))  # False
print(is_palindrome('HfwfxrDgh'))
