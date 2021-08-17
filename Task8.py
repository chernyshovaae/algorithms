year_ = int(input('Input year:\n'))

if (val / 10000) > 0 and (val / 10000) < 1:
    if year_ % 4 == 0:
        print('Temporal year')
    else:
        print('Non-temporal year ')
else:
    print('Input four -digit number')