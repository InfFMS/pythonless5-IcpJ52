# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
lst = list(map(int, input().split()))
cnt = 0
max_el = lst[0]
for el in lst:
    if el > max_el:
        max_el = el
        cnt = 1
    elif el == max_el:
        cnt += 1
print(cnt)
