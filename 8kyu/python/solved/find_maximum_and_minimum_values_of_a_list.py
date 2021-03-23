"""
https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
Your task is to make two functions,
max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list
as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples

maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0
#Notes

You may consider that there will not be any empty arrays/vectors.
"""


# my solution
def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


# other solution
def minimum(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low


def maximum(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high


# other solution
def minimum(arr):
    return sorted(arr)[0]


def maximum(arr):
    return sorted(arr)[-1]


# other solution

print('find min')
print(minimum([-52, 56, 30, 29, -54, 0, -110]))  # return result -110
print(minimum([42, 54, 65, 87, 0]))  # return result 0
print(minimum([1, 2, 3, 4, 5, 10]))  # return result 1
print(minimum([-1, -2, -3, -4, -5, -10]))  # return result -10
print(minimum([9]))  # return result 9

print('Find max')
print(maximum([-52, 56, 30, 29, -54, 0, -110]))  # return result 56
print(maximum([4, 6, 2, 1, 9, 63, -134, 566]))  # return result 566
print(maximum([5]))  # return result 5)
print(maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]))  # return result 555
print(maximum([9]))  # return result 9
