def return_day(day):
    days_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    if (day > 0) & (day < (len(days_of_week) + 1)):
        return days_of_week[day - 1]
    return None


print(return_day(7))


def return_day2(day):
    days_of_week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    if day in days_of_week:
        return days_of_week[day]
    return None


print(return_day2(10))