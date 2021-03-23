"""
https://www.codewars.com/kata/515e188a311df01cba000003/train/python
The function is not returning the correct values. Can you figure out why?

get_planet_name(3) # should return 'Earth'
"""

# my solution
db = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
}


def get_planet_name(_id):
    return db.get(_id)


# best solution
# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)


print(get_planet_name(2))  # return 'Venus'
print(get_planet_name(5))  # return 'Jupiter'
print(get_planet_name(3))  # return 'Earth'
print(get_planet_name(4))  # return 'Mars'
print(get_planet_name(8))  # return 'Neptune'
print(get_planet_name(1))  # return 'Mercury'
