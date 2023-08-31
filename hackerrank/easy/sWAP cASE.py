"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .
"""


def swap_case(s):
    new_string = ''
    for i in list(s):
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string


swap_case("Www.HackerRank.com")
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
