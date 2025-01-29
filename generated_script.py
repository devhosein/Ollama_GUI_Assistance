class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"The {self.species} named {self.name} says: {sound}")

# Creating instances of the class
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

# Calling methods on the objects
dog.make_sound("Woof!")
cat.make_sound("Meow!")

# Printing details about the animals
print(f"{dog.name} is a {dog.species}.")
print(f"{cat.name} is a {cat.species}.")