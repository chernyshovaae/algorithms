"""
1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
min_ = int(input('Диапазон делимых чисел от:\n'))
max_ = int(input('До:\n'))
min_n = int(input('Диапазон делителей от:\n'))
max_n = int(input('До:\n'))
print(f'Количество кратных чисел от {min_} до {max_} числам от {min_n} до {max_n}:')
""" 2, 99 + 1  """
lst = [i for i in range(min_, max_ + 1)]
""" 2, 9 + 1  """
lst_n = [i for i in range(min_n, max_n + 1)]

for i in range(len(lst_n)):
    s = 0
    for j in range(len(lst)):
        if lst[j] % lst_n[i] == 0:
            s += 1
    print(f'{lst[i]} - {s}')

