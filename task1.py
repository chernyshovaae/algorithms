"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict, namedtuple, Counter

num_company = int(input('Количество компаний:\n'))
count_ = 0
dt = defaultdict(list)
while count_ < num_company:
    name_ = input('Название компании:\n')
    for i in range(4):
        dt[name_].append(int(input(f'Прибыль {i + 1} квартал:\n')))
    count_ += 1

t = Counter({})
for i in dt:
    t[i] = sum(dt[i])
s = sum(t.values()) / num_company

for i in t:
    if t[i] > s:
        print(f'Предприятие с прибылью выше среднего ({s}): {i}')

for i in t:
    if t[i] <= s:
        print(f'Предприятие с прибылью ниже среднего ({s}): {i}')
