"""
https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
A hero is on his way to the castle to complete his mission.
However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated,
our hero has no idea how many bullets he should carry..
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons,
will he survive?

Return True if yes, False otherwise :)
"""


# my solution
def hero(bullets, dragons):
    while bullets >= dragons*2:
        return True
    else: return False


# Best Solution
# def hero(bullets, dragons):
#     return bullets >= dragons * 2

print(hero(10, 5))  # return True
print(hero(7, 4))  # return False
print(hero(4, 5))  # return False
print(hero(100, 40))  # return True
print(hero(1500, 751))  # return False
print(hero(0, 1))  # return False
