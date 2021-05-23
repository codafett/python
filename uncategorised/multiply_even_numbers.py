def multiply_even_numbers(values):
    evens = [val for val in values if val % 2 == 0]
    sum = evens[0]
    for val in evens[1:]:
        sum *= val
    return sum


print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48


def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48
