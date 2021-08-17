x1 = int(input('Input x1:\n'))
y1 = int(input('Input y1:\n'))
x2 = int(input('Input x2:\n'))
y2 = int(input('Input y2:\n'))

k = (y1 - y2) / (x1 - x2)
b = y2 - (k * x2)
print(f'y = {k}x + {b}')
