from Student import Student

with open("studenci.txt", "r", encoding="utf-8") as students:
    next(students)

    for student in students:
        student_interests = student.strip().split(',')
        if student_interests[0] == '':
            break

        next_student = Student(*student_interests)

# Nowy student, który przyjechał do Warszawy
# TODO: Naszym zadaniem jest polecenie naszemu studentowi nowych gatunków muzyki na podstawie pietnastu innych studentów
nowy_student = Student("Gwiezdne Wojny", "Kurczak curry",
                       "Złote Tarasy", "Klasyczna", 22)

# TODO: tutaj pobieramy tuple z rekomendowanymi gatunkami muzyki dla nowego studenta
recommended = nowy_student.recommend()

# print(TODO: Tutaj wywołaj pętle, która przeiteruje przez otrzymaną tuple i wyświetli polecane gatunki muzyki)
