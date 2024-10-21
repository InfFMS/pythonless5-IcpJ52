# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint

n = int(input())
lst = [randint(0, 1000) for _ in range(n)]
print(lst)
mean = sum(lst) / n
while True:
    try:
        lst.remove(1.3 * mean)
    except ValueError:
        break
while True:
    try:
        lst.remove(0.7 * mean)
    except ValueError:
        break
print(lst)
