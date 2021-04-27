user = {"name": "keith"}

print(user["name"])

# DON'T TOUCH PLEASE!
donations = dict(
    sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0
)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for v in donations.values():
    total_donations += v

# Alternatives
total_donations = sum(donation for donation in donations.values())
total_donations = sum(donations.values())

print(total_donations)

# This code picks a random food item:
from random import choice  # DON'T CHANGE!

food = choice(
    ["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"]
)  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25,
}

# YOUR CODE GOES BELOW:
stock = bakery_stock.get(food)
if stock:
    print("{} {} left".format(stock, food))
else:
    print("We don't make {}".format(food))

# DO NOT TOUCH game_properties!
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements",
]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)

inventory = {
    "croissant": 19,
    "bagel": 4,
    "muffin": 8,
    "cake": 1,
}  # DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = {}
stock_list.update(inventory)
print(stock_list)

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)

playlist = {
    "title": "Playlist 1",
    "songs": [{"title": "Song 1", "artist": "Artist 1"}],
}

print(playlist)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[n]: list2[n] for n in range(0, len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {p[0]: p[1] for p in person}
print(answer)

# alternatives
answer = {k: v for k, v in person}
answer = dict(person)

answer = {k: 0 for k in "aeiou"}
print(answer)

# alternative
answer = dict.fromkeys("aeiou", 0)

answer = {k: chr(k) for k in range(65, 91)}
print(answer)
