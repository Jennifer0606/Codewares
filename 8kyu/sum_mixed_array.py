"""
https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
"""


# my solution
def sum_mix(arr):
    return sum(int(arr[i]) for i in range((len(arr))))


# best soultion
def sum_mix(arr):
    return sum(map(int, arr))


# other soultion
def sum_mix(arr):
    return sum(int(n) for n in arr)

print(sum_mix([9, 3, '7', '3']))  # return 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # return 42
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # return 41
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))  # return 45
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))  # return 61
