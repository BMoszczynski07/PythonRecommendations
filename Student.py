from collections import Counter

students_interests = []


class Student:
    def __init__(self, film, jedzenie, miejsca, muzyka, wiek):
        self.film = film.lower()
        self.jedzenie = jedzenie.lower()
        self.miejsca = miejsca.lower()
        self.muzyka = muzyka.lower()
        self.wiek = int(wiek)

        self.add_student_interests()

    def recommend(self):
        # TODO: 1. Utwórz listę, która pobierze te zainteresowania studentów w students_interests, których wiek odpowiada wiekowi studenta w self.wiek
        # TODO: 2. Usuń z listy wyniki, w których ulubiona muzyka jest taka sama jak ulubiona muzyka analizowanego studenta w self.muzyka
        # TODO: 3. Za pomocą Countera policz w tablicy częstotliwość występowania poszczególnych gatunków muzyki w liście
        # TODO: 4. Na końcu w funkcji zwróć tuple o wartościach (<gatunek_muzyki>, <częstotliwość_występowania>)
        matching_intrerests = []
        for interest in students_interests:
            if interest[4] != self.wiek:
                continue
            if interest[3] == self.muzyka:
                continue

            matching_intrerests.append(interest[3]) 

        music_counter = Counter(matching_intrerests)

        print(music_counter)

    def add_student_interests(self):
        student_interests = [self.film,
                             self.jedzenie, self.miejsca, self.muzyka, self.wiek]

        students_interests.append(student_interests)

    def __str__(self):
        print(
            f"Student({self.film}, {self.muzyka}, {self.jedzenie}, {self.miejsca})")
