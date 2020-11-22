"""
https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python
Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special because it has the ability to change gravity.

There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of cubes might look like before and after switching gravity.

+---+                                       +---+
|   |                                       |   |
+---+                                       +---+
+---++---+     +---+              +---++---++---+
|   ||   |     |   |   -->        |   ||   ||   |
+---++---+     +---+              +---++---++---+
+---++---++---++---+         +---++---++---++---+
|   ||   ||   ||   |         |   ||   ||   ||   |
+---++---++---++---+         +---++---++---++---+
Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.

Examples:

flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]
"""


# My answer
def flip(d, a):
    if d == "R":
        a.sort()
    else:
        a.sort(reverse=True)
    return a


# Best practice
# def flip(d,a):
#     return sorted(a, reverse=d=='L')
#
# solution 1
# def flip(d, a):
#     if d == 'L':
#         return sorted(a, reverse=True)
#     else:
#         return sorted(a)


print(flip('R', [3, 2, 1, 2]))  # return  [1, 2, 2, 3]
print(flip('L', [1, 4, 5, 3, 5]))  # return [5, 5, 4, 3, 1]