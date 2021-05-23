def triple_and_filter(numbers):
    return list(num * 3 for num in numbers if num % 4 == 0)


print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]))  # [24,36])


def triple_and_filter(numbers):
    return list(map(lambda n: n * 3, filter(lambda n: n % 4 == 0, numbers)))


print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]))  # [24,36])