"""
https://www.codewars.com/kata/559f80b87fa8512e3e0000f5/train/python
Time to test your basic knowledge in functions! Return the odds from a list:

odds([1,2,3,4,5]) #=> [1,3,5]
"""


# my solution
# def odds(values):
#     result = []
#     for i in values:
#         if i % 2 == 1:
#             result.append(i)
#     return result


# best solution
def odds(values):
    return [i for i in values if i % 2]


print(odds([]))  # return []
print(odds([2, 4, 6]))  # return []
print(odds([1, 3, 5]))  # return [1, 3, 5]
print(odds([1, 2, 3, 4, 5, 6]))  # return [1, 3, 5]
