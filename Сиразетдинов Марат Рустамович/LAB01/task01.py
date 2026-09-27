a = input()
a = a.split()
b = [x for x in a]

def f(x):
    c = set(x)
    if len(x) != len(c):
        return "В последовательности есть повторяющиеся числа"
    else:
        return "Все числа в последовательности различны"

print(f(b))
    