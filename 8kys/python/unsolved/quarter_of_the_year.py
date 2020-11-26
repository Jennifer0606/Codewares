"""
https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter;
month 6 (June), is part of the second quarter;
and month 11 (November), is part of the fourth quarter.
"""


def quarter_of(month):
    season = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}
    for key, value in season.items():  # 回傳字典所有的鍵:值
        if month in value:
            return key


print(quarter_of(3))  # return 1
print(quarter_of(8))  # return 3
print(quarter_of(11))  # return 4
