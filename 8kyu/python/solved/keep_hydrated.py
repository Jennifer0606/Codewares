"""
https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""


# my solution
def litres(time):
    water = time / 2
    return int(water)


print(litres(2))  # 'should return 1 litre'
print(litres(1.4))  # 'should return 0 litres'
print(litres(12.3))  # 'should return 6 litres'
print(litres(0.82))  # 'should return 0 litres'
print(litres(11.8))  # 'should return 5 litres'
print(litres(1787))  # 'should return 893 litres'
print(litres(0))  # 'should return 0 litres'
