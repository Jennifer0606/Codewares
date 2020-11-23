input_arr = [0, 7, 5, 5, 6, 7, 100, 55]


new_arr = sorted(list(set(input_arr)))

for i in range((len(input_arr) - len(new_arr))):
    new_arr.append(new_arr[-1]+1)


print(new_arr)


def capitalize_word(word):
    return word.capitalize()

capitalize_word("jennifer")