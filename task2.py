"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import numpy

array = numpy.random.uniform(0.0, 49.0, size=10)
print(array)


def sort_merge(arr):
    if len(arr) < 2:
        return arr

    s = sort_merge(arr[:len(arr)//2])
    t = sort_merge(arr[len(arr)//2:len(arr)])
    i = 0
    j = 0
    res = []
    while i < len(s) or j < len(t):
        if not i < len(s):
            res.append(t[j])
            j += 1
        elif not j < len(t):
            res.append(s[i])
            i += 1
        elif s[i] < t[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(t[j])
            j += 1

    return res


print(sort_merge(array))
