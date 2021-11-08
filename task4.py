"""
4.	Определить, какое число в массиве встречается чаще всего.
"""
import random

min_ = int(input('Диапазон списка от:\n'))
max_ = int(input('До:\n'))
sz = int(input('Размер списка:\n'))
arr = [random.randint(min_, max_) for _ in range(sz)]
print('Исходный список:')
print(arr)
print('Количество чисел:')
for i in range(len(arr)):
    s = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            s += 1
    print(f'{arr[i]} - {s}')

