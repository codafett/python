class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "Hi, I'm {0}, who the hell are you?".format(self.name)


villager = NPC("bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())