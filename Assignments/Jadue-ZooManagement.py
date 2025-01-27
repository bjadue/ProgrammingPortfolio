# bjadue
# 4/18/24
# This program will manage a Zoo using classes and inheritance.

class Animal:

    def __init__(self, name, age, species, food_type):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__food_type = food_type

    def make_sound(self):
        print('"Schlamalaba woo woo"')

    def eat(self):
        print("I eat the souls of the damned")

    def display_info(self):
        print(f'\nName: {self.__name}\nAge: {self.__age}\nSpecies: {self.__species}\nFood Type: {self.__food_type}')

class Lion(Animal):

    def __init__(self, name, age, species, food_type, speech):
        Animal.__init__(self, name, age, species, food_type)
        Lion.__speech = speech

    def make_sound(self):
        print(f'"{Lion.__speech}"')

    def eat(self):
        print("I hunt other animals for food. I eat mainly meat.")

class Monkey(Animal):
    def __init__(self, name, age, species, food_type, speech):
        Animal.__init__(self, name, age, species, food_type)
        Monkey.__speech = speech

    def make_sound(self):
        print(f'"{Monkey.__speech}"')
    def alternate_sound(self):
        print(f"\nNow, I'm the king of the swingers\nOh, the jungle VIP\nI've reached the top and had to stop\nAnd that's what botherin' me")

    def eat(self):
        print("I eat a variety of fruits, leaves, seeds, nuts, flowers, vegetables, and insects.")

class Horse(Animal):
    def __init__(self, name, age, species, food_type, speech):
        Animal.__init__(self, name, age, species, food_type)
        Horse.__speech = speech

    def make_sound(self):
        print(f'"{Horse.__speech}"')

    def eat(self):
        print("I eat grains, fruits, hay, grass, and various plants.")


def main():
    '''
    default = Animal('PLCEHLDR', 00, 'PLCEHLDR', 'omnicarnivorni')
    default.display_info()
    default.make_sound()
    default.eat()
    '''
    lion = Lion('Alex', 26, 'Lion', 'Carnivore', 'Roar!')
    lion.display_info()
    lion.make_sound()
    lion.eat()

    monkey = Monkey('King Louie', 46, 'Arangatang', 'Omnivore', 'Oo oo aa aa!')
    monkey.display_info()
    monkey.make_sound()
#   monkey.alternate_sound()
    monkey.eat()

    horse = Horse('Bambi', 32, 'Horse', 'Herbivore', 'Neigh!')
    horse.display_info()
    horse.make_sound()
    horse.eat()
main()
