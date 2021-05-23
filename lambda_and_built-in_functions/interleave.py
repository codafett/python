def interleave(str1, str2):
    return "".join(("".join(z) for z in zip(str1, str2)))


print(interleave("hi", "ha"))  # hhia
print(interleave("aaa", "zzz"))  # azazaz
print(interleave("lzr", "iad"))  # lizard
