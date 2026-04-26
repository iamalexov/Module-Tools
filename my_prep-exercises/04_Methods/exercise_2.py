import datetime as dt

today = dt.date.today()


class Person:
    def __init__(self, name: str, birth_date: dt.date, preferred_operating_system: str) -> None:
        self.name = name
        self.birth_date = birth_date       
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        age = today.year - self.birth_date.year
        return age >= 18

imran = Person("Imran", dt.date(2000, 6, 21), "Ubuntu")

print(imran.is_adult())