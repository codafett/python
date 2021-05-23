class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.__mangled = "mangled"

    def print_mangled(self):
        print(self.__mangled)


c = Comment("u", "t")
c.print_mangled()