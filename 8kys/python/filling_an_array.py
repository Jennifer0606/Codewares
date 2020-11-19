"""
https://www.codewars.com/kata/571d42206414b103dc0006a1/train/python
We want an array, but not just any old array, an array with contents!

Write a function that produces an array with the numbers 0 to N-1 in it.

For example, the following code will result in an array containing the numbers 0 to 4:

arr(5) // => [0,1,2,3,4]
"""


# my answer
def arr(n=0):
    array = []
    while n == 0:
        return array
    for i in range(n):
        array.append(i)
    return array


# Best practice
# def arr(n=0):
#     return list(range(n))


print(arr(4))  # return[0, 1, 2, 3]
print(arr(0))  # return []
print(arr())  # return []
