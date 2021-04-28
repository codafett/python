# Define a function called generate_evens
# It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [n for n in range(1, 50) if n % 2 == 0]


result = generate_evens()

print(result)