def max_magnitude(values):
    absValues = map(lambda v: abs(v), values)
    return max(absValues)


print(max_magnitude([1, 2, 3, -4]))


def max_magnitude(values):
    return max(abs(num) for num in values)


print(max_magnitude([1, 2, 3, -90]))
