from datetime import date

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system



def is_adult(person: Person) -> bool:
    return person.age >= 18


imran = Person("Imran", 22, "Ubuntu")

print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)



print(is_adult(imran))


# exercise_02.py:20: error: "Person" has no attribute "address"  [attr-defined]
# exercise_02.py:24: error: "Person" has no attribute "address"  [attr-defined]