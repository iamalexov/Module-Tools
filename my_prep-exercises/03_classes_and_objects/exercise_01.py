class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")

print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

# alex@MacBook-Air-Oleksii classes_and_objects % mypy --strict  exercise_01.py 
# exercise_01.py:9: error: "Person" has no attribute "address"  [attr-defined]
# exercise_01.py:13: error: "Person" has no attribute "address"  [attr-defined]