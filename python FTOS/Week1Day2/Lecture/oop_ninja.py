

class Ninja:
    weapons = []
    # Contructor

    def __init__(self, name, health, belt):
        # these attributes are instance attributes
        self.name = name
        self.health = health
        self.power = 100
        self.belt = belt

        # - Instance methods
    def attack(self, another_ninja):
        another_ninja.health -= self.power/5
        return self

    def heal(self):
        self.health += 5

    def print_info(self):
        print("this ninja name is " + self.name)

        return self
