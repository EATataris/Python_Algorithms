"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?
import hashlib


def splitter(string):
    splitter_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                splitter_list.append(hashlib.sha256(string[i:j].encode()).hexdigest())
    return set(splitter_list)


print(len(splitter('рара')))


# def unique_subs(string):
#     return {hashlib.sha256(string[i:j].encode()).hexdigest() for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i:j] != string}
#
#
# print(len(unique_subs('рара')))