"""
https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/python
Task Overview
Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.

to_binary(1)  # should return 1
to_binary(5)  # should return 101
to_binary(11) # should return 1011
"""


# # my solution
# def to_binary(n):
#     return int("{0:b}".format(n))


# best solution
def to_binary(n):
    return int(f'{n:b}')


print(to_binary(1))  # 1    
print(to_binary(2))  # 10
print(to_binary(3))  # 11
print(to_binary(5))  # 101
