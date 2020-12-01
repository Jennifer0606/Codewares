"""
https://www.codewars.com/kata/50654ddff44f800200000007/train/python
Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.

The strings will not be the same length, but they may be empty ( length 0 ).

For example:

solution("1", "22") # returns "1221"
solution("22", "1") # returns "1221"
"""


# my solution
def solution(a, b):
    if len(a) > len(b):
        long = a
        short = b
    else:
        long = b
        short = a
    return short + long + short


# best solution
# def solution(a, b):
#     return a + b + a if len(a) < len(b) else b + a + b


print(solution('45', '1'))  # return '1451'
print(solution('13', '200'))  # return'1320013'
print(solution('Soon', 'Me'))  # return 'MeSoonMe'
print(solution('U', 'False'))  # return 'UFalseU'
