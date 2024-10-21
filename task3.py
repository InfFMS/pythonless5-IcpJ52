# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
from random import randint

n = int(input())
lst = [randint(0, 100) for _ in range(n)]
print(lst)
dct = {}
for i, num in enumerate(lst):
    if num in dct:
        dct[num].append(str(i))
    else:
        dct[num] = [str(i)]
max_lst = max(dct.values(), key=len)
if len(max_lst) == 1:
    print("Нет")
else:
    for num in dct.keys():
        if len(dct[num]) > 1:
            print(f"Значение: {num}, индексы: {', '.join(dct[num])}")
