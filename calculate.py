def calculate(make_float, operation, first, second, message=""):
    result = 0
    if operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    elif operation == "multiply":
        result = first * second
    else:
        result = first / second

    if make_float:
        result = float(result)
    else:
        result = int(result)

    if message:
        return "{0} {1}".format(message, result)
    return "The result is {0}".format(result)


print(
    calculate(
        make_float=False, operation="add", message="You just added", first=2, second=4
    )  # "You just added 6"
)

print(
    calculate(
        make_float=True, operation="divide", first=3.5, second=5
    )  # "The result is 0.7"
)

# Official solution
def calculate(**kwargs):
    operation_lookup = {
        "add": kwargs.get("first", 0) + kwargs.get("second", 0),
        "subtract": kwargs.get("first", 0) - kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) / kwargs.get("second", 0),
        "multiply": kwargs.get("first", 0) * kwargs.get("second", 0),
    }
    is_float = kwargs.get("make_float", False)
    operation_value = operation_lookup[kwargs.get("operation", "")]
    if is_float:
        final = "{} {}".format(
            kwargs.get("message", "The result is"), float(operation_value)
        )
    else:
        final = "{} {}".format(
            kwargs.get("message", "The result is"), int(operation_value)
        )
    return final