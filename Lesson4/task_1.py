"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


lst = list(range(100))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit('func_1(lst)', 'from __main__ import func_1, lst', number=1000))
print(timeit('func_2(lst)', globals=globals(), number=1000))

# Аналитика: в примере с func_2 я изменил фунцию, заменив наполнение списка с метода append на списковое включение
# тем самым уменьшив время исполнения функции