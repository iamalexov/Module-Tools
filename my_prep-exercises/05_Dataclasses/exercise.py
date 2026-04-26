import datetime as dt
from dataclasses import dataclass


today = dt.date.today()

@dataclass(frozen=True)
class Person:
    name: str
    birth_date: dt.date
    preferred_operating_system: str
       
    def is_adult(self) -> bool:
        age = today.year - self.birth_date.year
        return age >= 18

imran = Person("Imran", dt.date(2000, 6, 21), "Ubuntu")

print(imran)