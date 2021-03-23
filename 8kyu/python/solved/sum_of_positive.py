"""
https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


# my solution
# def positive_sum(arr):
#     result = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             result += arr[i]
#     return result


# best solution
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


print('Basic Test Cases')
print(positive_sum([1, 2, 3, 4, 5]))  # return 15
print(positive_sum([1, -2, 3, 4, 5]))  # return 13
print(positive_sum([-1, 2, 3, 4, -5]))  # return 9

print("returns 0 when array is empty")
print(positive_sum([]))  # return 0

print("returns 0 when all elements are negative")
print(positive_sum([-1, -2, -3, -4, -5]))  # return 0
