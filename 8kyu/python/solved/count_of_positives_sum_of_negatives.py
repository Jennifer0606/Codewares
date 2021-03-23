"""
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""


# my solution
def count_positives_sum_negatives(arr):
    pos_sum = 0
    neg_sum = 0
    while len(arr) == 0:
        return []
    # other solution of return []
    # if not arr: return []
    for i in arr:
        if i < 0:
            neg_sum += i
        elif i > 0:
            pos_sum += 1
    return [pos_sum, neg_sum]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  # [10, -65]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))  # [8, -50]
print(count_positives_sum_negatives([1]))  # [1, 0]
print(count_positives_sum_negatives([-1]))  # [0, -1]
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))  # [0, 0]
print(count_positives_sum_negatives([]))  # []
