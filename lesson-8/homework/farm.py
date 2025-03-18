class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")

    def lay_egg(self):
        return f"{self.name} laid an egg."


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")

    def shear_wool(self):
        return f"{self.name} is being sheared for wool."


cow = Cow("Bessie")
chicken = Chicken("Clucky")
sheep = Sheep("Wooly")

animals = [cow, chicken, sheep]
for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print(animal.sleep())
    if isinstance(animal, Cow):
        print(animal.produce_milk())
    elif isinstance(animal, Chicken):
        print(animal.lay_egg())
    elif isinstance(animal, Sheep):
        print(animal.shear_wool())

