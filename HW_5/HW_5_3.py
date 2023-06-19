# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib(n):
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2

fiban = fib(10)
print(next(fiban))
print(next(fiban))
print(next(fiban))
print(next(fiban))
print(next(fiban))
print(next(fiban))

