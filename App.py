"""
Title:       Critical Thinking Assignment #6
Author:      Minh Nguyen
Created:     2025-06-20
Last Edited: 2025-06-20
Description: This program is a comprehensive animal shelter management system that allows users to efficiently manage the shelter's animal inventory.
    Users can add new animals by providing details such as species, name, age, and breed or color, with input validation to ensure data integrity.
    The system maintains a list of animals currently housed, supports removing animals by name, and displays all animals with their details.
    A menu-driven interface guides users through adding animals, removing them, displaying the current shelter inventory, and exiting the program.
User Input:
    - Add animal with (species, name, age, breed/color)
    - Remove animal by name
    - View all animals currently in the shelter
    - Exit the program
Program Output:
    - Confirmation message upon adding or removing an animal
    - Animal-specific sounds upon addition ("Woof! Woof!" or "Meow! Meow!")
    - Display of the current list of animals with their details formatted in a table
    - Notifications when no animals are available to remove or display
"""

from abc import ABC, abstractmethod

# Abstract Animal class
class Animal(ABC):
    def __init__(self, name, age, species):
        self._name = name
        self._age = age
        self.species = species

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def update_age(self, new_age):
        self._age = new_age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def detail(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}, {self.detail()}")

# Dog subclass
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self._breed = breed

    def speak(self):
        print("Woof! Woof!")

    def detail(self):
        return f"Breed: {self._breed}"

# Cat subclass
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self._color = color

    def speak(self):
        print("Meow! Meow!")

    def detail(self):
        return f"Color: {self._color}"

# Abstract Shelter interface
class AnimalShelter(ABC):
    @abstractmethod
    def add_animal(self, animal):
        pass

    @abstractmethod
    def remove_animal(self, name):
        pass

    @abstractmethod
    def display_all(self):
        pass

# Shelter implementation
class Shelter(AnimalShelter):
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        animal.speak()
        print("Animal added successfully!")

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                self.animals.remove(animal)
                print("Animal removed successfully!")
                return
        print("Animal not found!")

    def display_all(self):
        if not self.animals:
            print("No animals currently in the shelter.")
            return

        print("\n{:<15} {:<5} {:<10} {:<20}".format("Name", "Age", "Species", "Detail"))
        print("-" * 55)
        for animal in self.animals:
            print("{:<15} {:<5} {:<10} {:<20}".format(animal.name, animal.age, animal.species, animal.detail()))

# Utility functions
def get_valid_input(prompt, condition, error_message):
    while True:
        value = input(prompt)
        if condition(value):
            return value
        print(error_message)

def main():
    shelter = Shelter()
    while True:
        print("\n--- Animal Shelter Management ---")
        print("1. Add Animal")
        print("2. Remove Animal")
        print("3. Display All Animals")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            species = get_valid_input(
                "Enter species (dog/cat): ",
                lambda x: x.lower() in ['dog', 'cat'],
                "Invalid input. Only 'dog' or 'cat' are accepted."
            ).lower()

            name = input("Enter name: ").strip()
            age = int(get_valid_input(
                "Enter age (number): ",
                lambda x: x.isdigit() and int(x) >= 0,
                "Invalid age. Please enter a non-negative number."
            ))

            if species == 'dog':
                breed = input("Enter breed: ").strip()
                animal = Dog(name, age, breed)
            else:
                color = input("Enter color: ").strip()
                animal = Cat(name, age, color)

            shelter.add_animal(animal)

        elif choice == '2':
            if not shelter.animals:
                print("No animals to remove.")
                continue
            shelter.display_all()
            name = input("Enter the name of the animal to remove: ").strip()
            shelter.remove_animal(name)

        elif choice == '3':
            shelter.display_all()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
