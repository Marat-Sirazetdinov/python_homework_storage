COURSES = [
    "Высшая математика",
    "Программирование",
    "Химия",
    "Биоинженерия",
    "История",
]
MIN_GRADE, MAX_GRADE = 2, 5


def main():
    students = {}

    print(f"Введите данные студента (курсы: {', '.join(COURSES)})")
    print("Для остановки ввода напишите 'стоп' в консоль")

    while True:
        name = input("Имя студента: ")
        if name == "стоп":
            break

        if name in students:
            print("Этот студент уже есть в системе!")
            continue

        grades = []
        print("Введите оценку по курсу от 2 до 5")

        for course in COURSES:
            while True:
                try:
                    grade = int(input(f"{course}: "))
                    if MIN_GRADE <= grade <= MAX_GRADE:
                        grades.append(grade)
                        break

                    print(
                        f"Оценка должна быть от {MIN_GRADE} до {MAX_GRADE}"
                    )
                except ValueError:
                    print("Некорректный ввод!")

        students[name] = grades
        print()

    if students:
        all_grades = [
            grade for grades in students.values() for grade in grades
        ]

        print("\nРезультаты:")

        for name, grades in students.items():
            print(
                f"{name}: {grades}, "
                f"среднее: {sum(grades) / len(grades):.2f}"
            )

        print("-" * 30)
        print(f"Общее кол-во студентов: {len(students)}")
        print(f"Общий средний балл: {sum(all_grades) / len(all_grades):.2f}")
        print(f"Минимальная оценка: {min(all_grades)}")
        print(f"Максимальная оценка: {max(all_grades)}")
    else:
        print("Нет данных о студентах.")


if __name__ == "__main__":
    main()
