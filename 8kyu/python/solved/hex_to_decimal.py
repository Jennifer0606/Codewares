"""
https://www.codewars.com/kata/57a4d500e298a7952100035d/train/python

Complete the function which converts hex number (given as a string) to a decimal number.
完成將十六進制數（以字符串形式給出）轉換為十進制數的函數。
"""


def hex_to_dec(s):
    return int(s, 16)


print(hex_to_dec("1"))
print(hex_to_dec("a"))
print(hex_to_dec("10"))
