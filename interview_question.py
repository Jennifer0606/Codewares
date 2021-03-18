"""
input = [0, 0, 1, 1]

return [0, 1, x, x]
x need to be Unique number
like [0, 1, 2, 4]
"""
input_arr = [0, 100, -50, 1, 100]

new_arr = sorted(list(set(input_arr)))

for i in range((len(input_arr) - len(new_arr))):
    new_arr.append(new_arr[-1] + 1)

print(new_arr)