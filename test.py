def apple(x):
    print(x)
    print(type(x))
    return "It's hotter than the sun!!" if pow(int(x), 2) > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


print(apple('50'))