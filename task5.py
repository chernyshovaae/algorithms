"""
5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

min_ = int(input('Диапазон списка от:\n'))
max_ = int(input('До:\n'))
sz = int(input('Размер списка:\n'))
arr = [random.randint(min_, max_) for _ in range(sz)]
print('Исходный список:')
print(arr)
num = 0
n_ind = 0
for i in range(len(arr)):
    if arr[i] > 0:
        continue
    if num == 0:
        num = arr[i]
        n_ind = i
    elif arr[i] > num:
        num = arr[i]
        n_ind = i
if num == 0:
    print('В списке нет отрицательных чисел')
else:
    print(f'Максимальное отрицательное число: {num}, позиция(индекс): {n_ind}')
