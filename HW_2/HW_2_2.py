# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from math import gcd

def sum_and_mul():
    num, den = map(int, input('Введите дробь: ').split('/'))
    num_2, den_2 = map(int, input('Введите дробь: ').split('/'))
    # если знаменатели равны
    if den == den_2:
        result = num + num_2
        print(f'Сумма дробей {result}/{den}')
        print(f'Произведение дробей {num * num_2}/{den * den_2}')
    else:
        cd = int(den * den_2 / gcd(den, den_2))
        rn = int(cd / den * num + cd / den_2 * num_2)
        g2 = gcd(rn, cd)
        total_num = int(rn / g2)
        total_den = int(cd / g2)
        print(f'Сумма дробей {total_num}/{total_den}')
        print(f'Произведение дробей {num * num_2}/{den * den_2}')

sum_and_mul()




