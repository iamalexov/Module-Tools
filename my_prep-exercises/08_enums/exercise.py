import sys
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
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


# 🔹 INPUT
name = input("Input name: ")

try:
    age = int(input("Input age: "))
except ValueError:
    print("Invalid age", file=sys.stderr)
    sys.exit(1)

try:
    preferred_os = OperatingSystem(input("Input operating system: "))
except ValueError:
    print("Invalid operating system", file=sys.stderr)
    sys.exit(1)


person = Person(name, age, preferred_os)


# 🔹 считаем ноутбуки
count = 0
for laptop in laptops:
    if person.preferred_operating_system == laptop.operating_system:
        count += 1

print(f"Available {count} laptops with {person.preferred_operating_system.value}")


# 🔹 совет
counts = Counter(l.operating_system for l in laptops)
best_os, best_count = counts.most_common(1)[0]

if best_os != person.preferred_operating_system:
    print(f"If you accept {best_os.value}, more laptops available: {best_count}")