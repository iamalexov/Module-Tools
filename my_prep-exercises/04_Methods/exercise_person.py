class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        return self.age >= 18

imran = Person("Imran", 22, "Ubuntu")

print(imran.is_adult())

# Methods are easier to understand because they belong to the class

# It is easier to find related logic in one place

# Methods use self, so they work directly with the object's data

# Methods improve encapsulation by keeping behavior close to the data