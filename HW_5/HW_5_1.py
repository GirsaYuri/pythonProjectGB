"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os



link = '/Users/girsa/PycharmProjects/pythonProjectGB/HW_4/HW_4_2.py '

def cut_link(way: str) -> tuple:
    path = os.path.abspath(way)
    name = os.path.basename(way)
    index = name.index('.')
    name_2 = name[:index]
    extenion = os.path.splitext(name)[1]
    my_tuple = [path, name_2, extenion]
    return tuple(my_tuple)

print(cut_link(link))
