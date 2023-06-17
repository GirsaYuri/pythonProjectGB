"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""

def rever(**kwargs):
    new_dict = {}
    for key, val in kwargs.items():
        try:
            if hash(val):
                result = {val: key}
                new_dict.update(result)
        except Exception:
            result = {str(val): key}
            new_dict.update(result)
    return new_dict


print(rever(чек=25, привет=72, my_list=[1, 2, 3], my_set = {1, 2, 3, 5, 6}))