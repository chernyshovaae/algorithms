val = int(input('Input three-digit number:\n'))

if (val / 1000) > 0 and (val / 1000) < 1:
    sum_val = (val // 100) + ((val % 100) // 10) + (val % 10)
    prod_val = (val // 100) * ((val % 100) // 10) * (val % 10)
    print(f'Sum: {sum_val}, Product: {prod_val}')
else:
    print('Input three-digit number')
