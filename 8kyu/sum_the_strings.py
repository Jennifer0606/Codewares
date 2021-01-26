"""
https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

  sum_str("4", "5")    # should output "9"
  sum_str("34", "5")   # should output "39"
If either input is an empty string, consider it as zero.
"""


# # my solution
# def sum_str(a, b):
#     if a == "" and b != "":
#         a = 0
#         result = a + int(b)
#     elif a != "" and b == "":
#         b = 0
#         result = int(a) + b
#     elif a == "" and b == "":
#         a = 0
#         b = 0
#         result = a + b
#     else:
#         result = int(a) + int(b)
#     return str(result)


# best solution
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


print(sum_str("4", "5"))  # return "9"
print(sum_str("34", "5"))  # return "39"
print(sum_str("9", ""))  # return "9", "x + empty = x"
print(sum_str("", "9"))  # return "9", "empty + x = x"
print(sum_str("", ""))  # return "0", "empty + empty = 0"
