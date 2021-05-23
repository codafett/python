def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return "{0}{1}".format(kwargs["prefix"], word)
    if "suffix" in kwargs:
        return "{0}{1}".format(word, kwargs["suffix"])
    return word


print(combine_words("child"))  # 'child'
print(combine_words("child", prefix="man"))  # 'manchild'
print(combine_words("child", suffix="ish"))  # 'childish'
print(combine_words("work", suffix="er"))  # 'worker'
print(combine_words("work", prefix="home"))  # 'homework'
