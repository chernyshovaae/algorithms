a = int(input('Legth a:\n'))
b = int(input('Legth b:\n'))
c = int(input('Legth c:\n'))

if a > (b + c) or b > (a + c) or c > (a + b):
    print('Triangle does not exists')
else:
    if a == b and b == c:
        print('Equilateral triangle')
    elif a == b or a == c or b == c:
        print('Isosceles triangle')
    else:
        print('Versatile triangle')
