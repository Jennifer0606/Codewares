"""
https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"].
The second one contains a student's submitted answers.

The two arrays are not empty and are the same length.
Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer,
and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
"""


# my solution
# def check_exam(arr1, arr2):
#     finally_score = 0
#     for i in range(len(arr1)):
#         if arr1[i] != arr2[i] and arr2[i] == "":
#             finally_score += 0
#         elif arr1[i] == arr2[i]:
#             finally_score += 4
#         else:
#             finally_score -= 1
#     return 0 if finally_score < 0 else finally_score


# best solution
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))  # return 6
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))  # return 7
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))  # return 16
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))  # return 0
