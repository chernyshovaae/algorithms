letters = 'abcdefghijklmnopqrstuvwxyz'
letter1 = input('Input letter 1:\n')
letter2 = input('Input letter 2:\n')
indx_1 = letters.index(letter1)
indx_2 = letters.index(letter2)
if indx_1 < indx_2:
    len_ = len(letters[indx_1:indx_2]) - 1
else:
    len_ = len(letters[indx_2:indx_1]) - 1
print(f'Num letter 1: {indx_1 + 1}, num letter 2: {indx_2 + 1}, amount letters between letter 1 and letter 2: {len_}')