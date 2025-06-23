class Animal:
    def make_sound(self):  # Parent method
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):  # Overridden method
        print("guau!")

class Cat(Animal):
    def make_sound(self):  # Overridden method
        print("Miau!")

# Polymorphism in action
def animal_sound(animal):
    animal.make_sound()

# Using the parent reference for different child objects
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal_sound(animal)
