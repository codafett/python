import keyword


def contains_keyword(*args):
    return any(keyword.iskeyword(k) for k in args)


print(contains_keyword("if"))
