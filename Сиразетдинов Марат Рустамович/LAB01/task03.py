import string

PUNCTUATION = list(string.punctuation)
all_russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
russian_vowels = "аеёиоуыэюя"
CONSONANTS = [char for char in all_russian if char not in russian_vowels and char not in "ъь"]

input_string = input("Введите строку слов на русском языке:\n ").strip()

if not input_string:
    print("Вы ввели пустую строку!")

else:
    words_list = input_string.split()
    words_tuple = tuple(words_list)

    print(f"Всего слов в кортеже: {len(words_tuple)}")

    unique_words = set(words_tuple)
    print(f"Количество уникальных слов: {len(unique_words)}")

total_vowels = 0
word_vowels_count = 0
for char in input_string.lower():
    if char in russian_vowels:
        word_vowels_count += 1

    total_vowels += word_vowels_count

print(f"Гласных:{word_vowels_count}")

total_consonants = 0
word_consonants_count = 0
for char in input_string.lower():
    if char in CONSONANTS:
        word_consonants_count += 1

    total_consonants += word_consonants_count

print(f"Согласных:{word_consonants_count}")

total_punctuation = 0
word_punctuation_count = 0
for char in input_string.lower():
    if char in PUNCTUATION:
        word_punctuation_count += 1

    total_punctuation += word_punctuation_count

print(f"Знаков препинания:{word_punctuation_count}")