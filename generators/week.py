def week():
    count = 0
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    while count < 7:
        day = days[count]
        yield day
        count += 1


w = week()
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))


def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    for day in days:
        yield day