def list_manipulation(list, command, location, value=None):
    result = list
    if command.lower() == "add":
        if location.lower() == "beginning":
            list.insert(0, value)
        if location.lower() == "end":
            list.append(value)
    if command.lower() == "remove":
        if location.lower() == "beginning":
            result = list.pop(0)
        if location.lower() == "end":
            result = list.pop()
    return result


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  #  1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  #  [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  #  [1,2,3,30]
