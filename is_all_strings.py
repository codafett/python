def is_all_strings(values):
    return all(type(val) is str for val in values)


print(is_all_strings(["a", "b", "c"]))
print(is_all_strings([2, "b", "c"]))
print(is_all_strings(("hello", "goodbye")))
