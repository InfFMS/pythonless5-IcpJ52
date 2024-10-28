# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей: [10, 20, 30, 40, 50]
from random import randint

n = int(input())
lst = [randint(-100, 100) for _ in range(n)]
print(lst)
print(list(set(lst)))
