from pyfiglet import figlet_format
from termcolor import colored

col = input("Pick colour: ")
print("\n")
word = input("Pick a word: ")
print("\n")

print(colored(figlet_format(word), col))
