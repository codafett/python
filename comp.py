answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
print(answer)

answer = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(answer)

answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5]]
print(answer)

answer = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer)

answer = [val for val in range(1, 101) if val % 12 == 0]
print(answer)

answer = [letter for letter in "amazing" if letter not in "aeiou"]
print(answer)

answer = [list(range(0, 3)) for l in range(1, 4)]
print(answer)

answer = [list(range(0, 10)) for l in range(0, 10)]
print(answer)