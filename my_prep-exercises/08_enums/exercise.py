import sys
from dataclasses import dataclass
from enum import Enum


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


name = input("Name: ")

age_input = input("Age: ")
try:
    age = int(age_input)
except ValueError:
    print("Wrong age")
    sys.exit(1)


os_input = input("OS (Ubuntu / Arch Linux / macOS): ")
try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print("Wrong OS")
    sys.exit(1)


person = Person(name, age, preferred_os)


count = 0
for laptop in laptops:
    if laptop.operating_system == person.preferred_operating_system:
        count += 1

print("Laptops available:", count)


max_count = 0
best_os = None

for laptop in laptops:
    c = 0
    for l in laptops:
        if l.operating_system == laptop.operating_system:
            c += 1

    if c > max_count:
        max_count = c
        best_os = laptop.operating_system


if best_os is not None and best_os != person.preferred_operating_system:
    print("Better choose:", best_os.value)