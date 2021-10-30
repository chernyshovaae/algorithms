"""
6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

alh = 'abcdefghijklmnopqrstuvwxyz'
num = int(input('Номер символа a-z:\n'))

if 0 < num <= 26:
    s = alh[num - 1]
    print(f'Символ: {s}')
else:
    print('Номер вне алфавита')

