"""
https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
"""


# my answer
def areYouPlayingBanjo(name):
    return "{} plays banjo".format(name) if name.lower()[0] == "r" else "{} does not play banjo".format(name)

# best practices
# def areYouPlayingBanjo(name):
#     return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"


print(areYouPlayingBanjo("martin"))  # return "martin does not play banjo""
print(areYouPlayingBanjo("Rikke"))  # return "Rikke plays banjo"
