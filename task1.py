"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9

"""
import hashlib


def hash_list(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()


def func_substr(val):
    l, n = 1, 0
    lst = []
    count_ = 0
    while l < len(val):
        for i in range(len(val) - n):
            el_ = val[i:i + l]
            if hash_list(el_) not in lst:
                lst.append(hash_list(el_))
        n, l = n + 1, l + 1
    return len(lst)


s = input('Введите строку:\n')
print(func_substr(s))

