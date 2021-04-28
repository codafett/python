def yell(phrase):
    """First function"""
    return "{}!".format(phrase.upper())


yell()
print(yell.__doc__)
print(yell("go away"))
