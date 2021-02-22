"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    res = max(zip((array.count(el) for el in set(array)), set(array)))
    return f'Чаще всего встречается число {res[1]}, ' \
           f'оно появилось в массиве {res[0]} раз(а)'


def func_4():
    max_lst = [array.count(el) for el in array]
    elem = array[max_lst.index(max(max_lst))]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max(max_lst)} раз(а)'


def func_5():
    lst = {array.count(val): val for val in set(array)}
    return f'Чаще всего встречается число {lst[sorted(lst.keys(), reverse=True)[0]]}, ' \
           f'оно появилось в массиве {sorted(lst.keys(), reverse=True)[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())


print(timeit('func_1()', globals=globals(), number=10000))
print(timeit('func_2()', globals=globals(), number=10000))
print(timeit('func_3()', globals=globals(), number=10000))
print(timeit('func_4()', globals=globals(), number=10000))
print(timeit('func_5()', globals=globals(), number=10000))

'''
Аналитика. С помощью написанных мною 3 новых функций ускорить задачу не удалось. Самым быстрым и лучшим вариантом
явялеяется первая функция. На ее исполнение затрачивается меньше всего времени
'''