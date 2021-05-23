def divide(num1, num2):
    if (type(num1) is not float and type(num1) is not int) or (
        type(num2) is not float and type(num2) is not int
    ):
        return "Please provide two integers or floats"
    elif num2 == 0:
        return "Please do not divide by zero"
    return num1 / num2


print(divide(4, 2))  #  2
print(divide([], "1"))  #  "Please provide two integers or floats"
print(divide(1, 0))  #  "Please do not divide by zero"


def divide(a, b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total


print(divide(4, 2))  #  2
print(divide([], "1"))  #  "Please provide two integers or floats"
print(divide(1, 0))  #  "Please do not divide by zero"
