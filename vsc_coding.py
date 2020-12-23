# Let's finally write up some Python code using Visual Studio Code and see how this will feel in my Raspberry Pi.

class Player:
    def __init__(self, name, health, magic, lvl):
        self.name   = name
        self.health = health
        self.magic  = magic
        self.lvl    = lvl

    def print_stats(self):
        print(f'Name: {self.name} Health: {self.health} Magic: {self.magic} Level: {self.lvl}')

    def set_stats(self, name, health, magic, lvl):
        self.name   = name
        self.health = health
        self.magic  = magic
        self.lvl    = lvl


player_one = Player('Groku', 99, 199, 3)
player_one.print_stats()
player_one.set_stats('Groot', 50, 100, 1)
player_one.print_stats()




        