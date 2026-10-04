import string

PUNCTUATION = list(string.punctuation)
ALL_RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUSSIAN_VOWELS = "аеёиоуыэюя"
CONSONANTS = [
    char
    for char in ALL_RUSSIAN
    if char not in RUSSIAN_VOWELS and char not in "ъь"
]


def main():
    input_string = input("Введите строку слов на русском языке:\n ").strip()

    if not input_string:
        print("Вы ввели пустую строку!")
        return

    words_list = input_string.split()
    words_tuple = tuple(words_list)

    print(f"Всего слов в кортеже: {len(words_tuple)}")

    unique_words = set(words_tuple)
    print(f"Количество уникальных слов: {len(unique_words)}")

    word_vowels_count = 0
    for char in input_string.lower():
        if char in RUSSIAN_VOWELS:
            word_vowels_count += 1

    print(f"Гласных: {word_vowels_count}")

    word_consonants_count = 0
    for char in input_string.lower():
        if char in CONSONANTS:
            word_consonants_count += 1

    print(f"Согласных: {word_consonants_count}")

    word_punctuation_count = 0
    for char in input_string.lower():
        if char in PUNCTUATION:
            word_punctuation_count += 1

    print(f"Знаков препинания: {word_punctuation_count}")


if __name__ == "__main__":
    main()
