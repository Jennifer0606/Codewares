"""
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
Complete the solution so that it reverses the string passed into it.
"""


# my solution
def solution(string):
    return ''.join(reversed(string))


# best solution
# def solution(string):
#     return string[::-1]


print(solution('world'))  # return 'dlrow'
print(solution('hello'))  # return 'olleh'
print(solution(''))  # return ''
print(solution('h'))  # return 'h'
