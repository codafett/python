def yes_or_no():
    result = ""
    while True:
        if result == "yes":
            result = "no"
        else:
            result = "yes"
        yield result


y = yes_or_no()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"