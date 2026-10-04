ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя ")


def main():
    print("Введите текст или числа через дефис")
    print("Для завершения работы напишите 'стоп'\n")

    while True:
        user_input = input("Введите данные: ")

        if user_input.lower() == "стоп":
            break

        if user_input.replace("-", "").isdigit():
            num_list = user_input.split("-")
            letters = []

            for num_str in num_list:
                if num_str.isdigit():
                    num = int(num_str)
                    if 1 <= num <= len(ALPHABET):
                        letters.append(ALPHABET[num - 1])

            print("Расшифрованный текст:", "".join(letters))

        else:
            numbers = []

            for letter in user_input.lower():
                if letter in ALPHABET:
                    num = ALPHABET.index(letter) + 1
                    numbers.append(str(num))

            print("Зашифрованные числа:", "-".join(numbers))


if __name__ == "__main__":
    main()

