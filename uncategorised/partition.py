def isEven(num):
    return num % 2 == 0


def partition(values, callback):
    evens = []
    odds = []
    for val in values:
        if callback(val):
            evens.append(val)
        else:
            odds.append(val)
    return [evens, odds]


print(partition([1, 2, 3, 4], isEven))  # [[2,4],[1,3]]
