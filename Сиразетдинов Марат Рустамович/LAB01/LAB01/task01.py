def check_duplicates(sequence):
    unique_elements = set(sequence)
    if len(sequence) != len(unique_elements):
        return "В последовательности есть повторяющиеся числа"

    return "Все числа в последовательности различны"


def main():
    user_input = input("Введите элементы через пробел: ")
    elements = user_input.split()

    result = check_duplicates(elements)
    print(result)


if __name__ == "__main__":
    main()
