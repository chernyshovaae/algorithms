a = int(input('Input first num:\n'))
b = int(input('Input second num:\n'))
c = int(input('Input third num:\n'))

if (a > b and a < c) or (a < b and a > c):
    res = a
elif (b > a and b < c) or (b < a and b > c):
    res = b
elif (c > a and c < b) or (c < a and c > b):
    res = c
else:
    print('Some numbers are equal')
print(f'Average num: {res}')
