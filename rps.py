import random

computerInt = random.randint(0, 2)
computerChoice = "rock"
if computerInt == 1:
    computerChoice = "paper"
elif computerInt == 2:
    computerChoice = "scissors"

print("...rock...")
print("...paper...")
print("...scissors...")
p1 = input("(enter Player 1's choice): ").lower()
print(f"(computer chose): {computerChoice}")
print("SHOOT!")
win = 0
if p1 != computerChoice:
    if p1 == "rock" and computerChoice == "scissors":
        win = 1
    elif p1 == "paper" and computerChoice == "rock":
        win = 1
    elif p1 == "scissors" and computerChoice == "paper":
        win = 1
    else:
        win = 2

if win == 1:
    print("player1 wins")
elif win == 2:
    print("player2 wins")
else:
    print("draw")
