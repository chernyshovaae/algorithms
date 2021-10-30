"""
5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

letters = 'abcdefghijklmnopqrstuvwxyz'
letter1 = input('Введите первый символ:\n')
letter2 = input('Введите второй символ:\n')
one_num = letters.index(letter1)
two_num = letters.index(letter2)
if one_num < two_num:
    amt = len(letters[one_num:two_num]) - 1
else:
    amt = len(letters[two_num:one_num]) - 1
print(f'Позиция первого символа: {one_num + 1}, Позиция второго символа: {two_num + 1},' +
      f' кол-во символов между ними: {amt}')
