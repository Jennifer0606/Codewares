"""
https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""


# my solution
# def lovefunc(flower1, flower2):
#     if flower1 % 2 == 1 and flower2 % 2 == 0:
#         return True
#     elif flower1 % 2 == 0 and flower2 % 2 == 1:
#         return True
#     else: return False


# best solution
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2


print(lovefunc(1, 4))  # return True
print(lovefunc(2, 2))  # return False
print(lovefunc(0, 1))  # return True
print(lovefunc(0, 0))  # return False
