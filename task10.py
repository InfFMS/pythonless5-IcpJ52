# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
from random import randint
from math import acos, pi

n = int(input())
a = [randint(-100, 100) for _ in range(n)]
b = [randint(-100, 100) for _ in range(n)]
scalar = sum([a[i] * b[i] for i in range(n)])
len_a = (sum([x ** 2 for x in a])) ** 0.5
len_b = (sum([x ** 2 for x in b])) ** 0.5
angle = acos(scalar / (len_a * len_b)) * 180 / pi
print('Вектор a:', a)
print('Вектор b:', b)
print(f'Угол между векторами: {angle}')
