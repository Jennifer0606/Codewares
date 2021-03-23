"""
https://www.codewars.com/kata/587c2d08bb65b5e8040004fd/train/python
一場NBA遊戲運行48分鐘（每四個季度12分鐘）。 玩家通常不會玩完整的遊戲，而是在必要時進出。
您的工作是如果玩家玩了整整48分鐘，則推斷出他們每場比賽的得分。
編寫一個函數，該函數需要兩個參數，ppg（每場比賽的積分）和 mpg（每場比賽的分鐘數）
並返回每 48 分鐘四捨五入的 ppg 的直推法，以最接近的十分。返回 0（如果為 0）
An NBA game runs 48 minutes (Four 12 minute quarters).
Players do not typically play the full game, subbing in and out as necessary.
Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game)
and returns a straight extrapolation of ppg per 48 minutes rounded to the nearest tenth. Return 0 if 0.

Examples:

nba_extrap(12, 20) # 28.8
nba_extrap(10, 10) # 48
nba_extrap(5, 17) # 14.1
nba_extrap(0, 0) # 0
Notes:
All inputs will be either be an integer or float.
Follow your dreams!
"""


def nba_extrap(ppg, mpg):
    return round(ppg * 48.0 / mpg, 1) if mpg else 0


print(nba_extrap(12, 20))  # return  28.8
print(nba_extrap(10, 10))  # return  48.0
print(nba_extrap(5, 17))  # return  14.1
print(nba_extrap(0, 0))  # return  0
print(nba_extrap(30.8, 34.7))  # return  42.6
print(nba_extrap(22.9, 33.8))  # return  32.5
