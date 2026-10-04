import math


def main():
    print("Для завершения работы напишите 'стоп' вместо числа\n")

    while True:
        user_input_a = input("Введите длину первого катета: ").strip()
        if user_input_a.lower() == "стоп":
            break

        user_input_b = input("Введите длину второго катета: ").strip()
        if user_input_b.lower() == "стоп":
            break

        try:
            a = float(user_input_a)
            b = float(user_input_b)

            if a <= 0 or b <= 0:
                print("Ошибка: Длина стороны должна быть больше нуля!\n")
                continue

            c = math.sqrt(a**2 + b**2)
            print(f"-> Длина гипотенузы: {c:.2f}")

            print()

        except ValueError:
            print("Ошибка: Нужно вводить только числа\n")


if __name__ == "__main__":
    main()
