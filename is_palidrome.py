def is_palindrome(val):
    index = 0
    result = True
    while index < len(val):
        if val[index] != val[(index + 1) * -1]:
            result = False
            break
        index += 1
    return result


print(is_palindrome("wordrw"))


def is_palindrome(val):
    stripped = val.replace(" ", "")
    return stripped == stripped[::-1]


print(is_palindrome("worddrow"))
