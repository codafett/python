def frequency(val, search):
    return val.count(search)


print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
print(frequency([True, False, True, True], False))  # 1
