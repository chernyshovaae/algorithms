letters = 'abcdefghijklmnopqrstuvwxyz'
num_let = int(input('Num letter:\n'))
if num_let > 0 and num_let <= 26:
    letter = letters[num_let - 1]
else:
    print('Out of range')
print(f'Letter: {letter}')