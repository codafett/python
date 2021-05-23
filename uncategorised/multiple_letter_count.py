def multiple_letter_count(word):
    return {letter: word.upper().count(letter.upper()) for letter in word}


print(multiple_letter_count("hello"))
