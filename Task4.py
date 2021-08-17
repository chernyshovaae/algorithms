import random

a = int(input('Begin range int:\n'))
b = int(input('End range int:\n'))

int_num = random.randint(a, b)
print(int_num)

a = int(input('Begin range float:\n'))
b = int(input('End range float:\n'))
float_num = random.uniform(a, b)
print(float_num)

letters = input('List letters:\n')
letter_ = random.choice(letters)
print(letter_)