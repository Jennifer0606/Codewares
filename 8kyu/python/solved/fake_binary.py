"""
https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.
"""


# my solution
def fake_bin(x):
    for i in "01234":
        x = x.replace(i, "0")
    for j in "56789":
        x = x.replace(j, "1")
    return x


# best solution
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)


# other solution
# def fake_bin(s):
#   return ''.join('0' if int(c) < 5 else '1' for c in s)


print(fake_bin("45385593107843568"))  # return "01011110001100111"
print(fake_bin("509321967506747"))  # return "101000111101101"
print(fake_bin("366058562030849490134388085"))  # return "011011110000101010000011011"
print(fake_bin("15889923"))  # return "01111100"
print(fake_bin("800857237867"))  # return "100111001111"
