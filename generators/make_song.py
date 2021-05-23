def make_song(count=99, beverage="soda"):
    index = count
    while index >= 0:
        if index == 0:
            yield "No more {0}!".format(beverage)
        elif index == 1:
            yield "Only 1 bottle of {0} left!".format(beverage)
        else:
            yield "{0} bottles of {1} on the wall.".format(index, beverage)
        index -= 1


song = make_song(5, "beer")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
