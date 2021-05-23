class Chicken:
    total_eggs = 0

    @classmethod
    def get_total_eggs(cls):
        return cls.total_eggs

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1


c1 = Chicken("a", "a")
c2 = Chicken("b", "b")
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c1.lay_egg()
c2.lay_egg()
print(f"c1 has laid {c1.eggs} eggs")
print(f"c2 has laid {c2.eggs} eggs")
print(f"{Chicken.get_total_eggs()} eggs have been laid in total")
