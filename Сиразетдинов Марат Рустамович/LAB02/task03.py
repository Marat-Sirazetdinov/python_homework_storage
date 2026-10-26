def multiply_by_two(*args):
    """
    Находит произведение всех целых чисел
    :param args:Произвольные аргументы
    :return:Строка с результатом произведения целых чисел и информация о типах данных
    """
    integers = [x for x in args if type(x) is int]

    if integers:
        start = 1
        for num in integers:
            start *= num
        return f"Произведение целых числе: {start}"

    args_info = [f" '{x}'- {type(x).__name__}" for x in args]
    return args_info


def parse_input(user_input):
    """
    Разбирает строку чисел на int, float или оставляет строками
    :param user_input: Строка
    :return: Список элементов, приведенный к соответствующим типам данных
    """
    parsed_args = []

    for item in user_input.split():
        if item.isdigit() or (item.startswith("-") and item[1:].isdigit()):
            parsed_args.append(int(item))
        else:
            try:
                parsed_args.append(float(item))
            except ValueError:
                parsed_args.append(item)
    return parsed_args


if __name__ == '__main__':
    raw_input = input("Введите аргументы через пробел:\n")

    arguments = parse_input(raw_input)

    result = multiply_by_two(*arguments)
    print(f"\n{result}")
