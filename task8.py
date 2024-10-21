# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint


def is_same_digits(num):
    return len(set(str(num))) == 1


n = int(input())
lst = [randint(10, 100000) for _ in range(n)]
print(lst)
res = []
for el in lst:
    if is_same_digits(el):
        res.append(el)
print(res)
