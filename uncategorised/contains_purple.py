def contains_purple(*args):
    return "purple" in args


print(contains_purple(25, "purple"))  # True
print(contains_purple("green", False, 37, "blue", "hello world"))  # False
print(contains_purple("purple"))  # True
print(contains_purple("a", 99, "blah blah", 1, True, False, "purple"))  # True
print(contains_purple(1, 2, 3))  # False
