# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# 1. Обычное решение
name = ['Игорь', 'Вася', 'Петя', 'Гена']
stack = [25, 72, 42, 51]
prem = ['10.25%', '18%', '7.5%', '1%']
def premia(name, stack, prem):
    dict_prem = {}
    for index, name in enumerate(name):
        dict_prem[name] = stack[index] * (float(prem[index][0:-1]) + 100) / 100
    return dict_prem

print(premia(name, stack, prem))

# 2. Генератор (честно - пока сложно читать такой код, точнее понимать логику работы)
selary = {name: (stack[index] * (float(prem[index][0:-1]) + 100) / 100) for index, name in enumerate(name)}
print(selary)