# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.append("Colt")
instructors.extend(["Blue", "Lisa"])
print(instructors)

# Remove the last value in the list
instructors.pop()
print(instructors)

# Remove the first value in the list
instructors.pop(0)
print(instructors)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")
print(instructors)

numbers = [1, 2, 3, 4]
print(numbers[1:3])
