def single_letter_count(word, letter):
    return word.upper().count(letter.upper())


print(single_letter_count("Hello world", "h"))
print(single_letter_count("Hello world", "z"))
print(single_letter_count("Hello world", "l"))
