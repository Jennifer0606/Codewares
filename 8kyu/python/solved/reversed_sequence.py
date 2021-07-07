"""
https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 >> [5,4,3,2,1]
"""


# my solution
def reverse_seq(n):
    res = [i for i in range(1, n + 1)]
    res.reverse()
    return res


# best solution
# def reverse_seq(n):
#     return list(range(n, 0, -1))


# other solution
# def reverse_seq(n):
#     return [x for x in range(n, 0, -1)]


print(reverse_seq(5))  # return [5,4,3,2,1]
