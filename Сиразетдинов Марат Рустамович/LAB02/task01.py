def filter_of_average(strings):
    """
    Фильтрует список строк,
    :param strings:Список строк для анализа
    :return:Список строк, длинна которых превышает среднюю, либо ошибку, если пустой ввод
    """
    if not strings:
        return "Вы ничего не ввели!"

    avg = sum(len(s) for s in strings) / len(strings)
    return list(filter(lambda s: len(s) > avg, strings))


if __name__ == "__main__":
    strings: list[str] = input("Ведите строки через пробел:\n").split()

    result = filter_of_average(strings)
    print(result)

