"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

"""
import random

min_ = int(input('Диапазон списка от:\n'))
max_ = int(input('До:\n'))
sz = int(input('Размер списка:\n'))
arr = [random.randint(min_, max_) for _ in range(sz)]
print('Исходный список:')
print(arr)
min_el = arr[0]
min_el_t = 0
for i in range(len(arr)):
    if arr[i] <= min_el:
        min_el_t = min_el
        min_el = arr[i]

print(f'Два минимальных числа: {min_el} и {min_el_t}')
