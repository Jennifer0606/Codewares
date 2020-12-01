"""
https://www.codewars.com/kata/55eea63119278d571d00006a/train/python
Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!
"""


# my solution
def next_id(arr):
    arr.sort()
    for i in range(len(arr) + 1):
        if i not in arr:
            return i


print(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # return 11
print(next_id([5, 4, 3, 2, 1]))  # return 0
print(next_id([0, 1, 2, 3, 5]))  # return 4
print(next_id([0, 0, 0, 0, 0, 0]))  # return 1
print(next_id([]))  # return 0
