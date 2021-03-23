"""
https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
Our football team finished the championship. The result of each match look like "x:y".
Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship.
Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


# my solution
# def points(games):
#     total_scr = 0
#     for i in range(len(games)):
#         if games[i][0] > games[i][2]:
#             total_scr += 3
#         elif games[i][0] == games[i][2]:
#             total_scr += 1
#         else:
#             total_scr += 0
#     return total_scr


# best solution
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))  # return 30
print(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']))  # return 10
print(points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4']))  # return 0
print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']))  # return 15
print(points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']))  # return 12
