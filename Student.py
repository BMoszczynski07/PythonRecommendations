class Student:
    def __init__(self, filmy, jedzenie, miejsca, muzyka):
        self.filmy = filmy
        self.jedzenie = jedzenie
        self.miejsca = miejsca
        self.muzyka = muzyka

    def __str__(self):
        print(f"Student({self.filmy}, {self.muzyka}, {self.jedzenie}, {self.miejsca})")