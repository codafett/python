def intersection(list1, list2):
    return [val for val in set(list1).intersection(set(list2))]


print(intersection([1, 2, 3], [2, 3]))  # [2,3]
print(intersection(["a", "b", "z"], ["x", "y", "z"]))  # ['z]

# Shorthand
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]


print(intersection([1, 2, 3], [2, 3]))  # [2,3]
print(intersection(["a", "b", "z"], ["x", "y", "z"]))  # ['z]
