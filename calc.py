# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:


for num in range(10, 20):
    if num % 2 != 0:
        print(f'adding {num}')
        x = x + num
        
print(x)