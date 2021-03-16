"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import timeit

simple_list = list('abc')
deque_list = deque(simple_list)


def list_append(x):
    for i in range(x):
        simple_list.append(i)
    return simple_list


def deque_list_append(x):
    for i in range(x):
        deque_list.append(x)
    return deque_list


def list_pop():
    simple_list.pop()
    return simple_list


def deque_list_pop():
    deque_list.pop()
    return simple_list


def list_remove():
    simple_list.remove(simple_list[0])
    return simple_list


def deque_list_pop_left():
    deque_list.popleft()
    return deque_list


def list_insert(x):
    simple_list.insert(0, x)
    return simple_list


def deque_appendleft(x):
    deque_list.appendleft(x)
    return deque_list


n = 100
'''
Аналитика: Методы list.append и deque.append то есть добавление эл-тов в конец списка выполняются с одинаковой скоростью
как для обычного списка, так и для дека из модуля коллекций
'''
print(timeit('list_append(n)', globals=globals(), number=1000))
print(timeit('deque_list_append(n)', globals=globals(), number=1000), end='\n\n')

'''
Аналитика: Методы list.pop и deque.pop то есть добавление удаление эл-та с конеца списка выполняются с одинаковой скоростью
как для обычного списка, так и для дека из модуля коллекций.
'''
print(timeit('list_pop()', globals=globals(), number=10000))
print(timeit('deque_list_pop()', globals=globals(), number=10000), end='\n\n')

'''
Аналитика: в Данном примеер видно, что одиноковые по семантике методы удаления эл-та с начала списка в деке выполняется
значительно быстрее. Приблизительно в 60 раз!
'''
print(timeit('list_remove()', globals=globals(), number=10000))
print(timeit('deque_list_pop_left()', globals=globals(), number=10000), end='\n\n')

'''
Аналитика: в данном примеер видно, что одиноковые по семантики методы доавления эл-та в начало списка в деке выполняется
значительно быстрее. Разница коллосалльная более чем в 180 раз!
'''
print(timeit('list_insert(n)', globals=globals(), number=10000))
print(timeit('deque_appendleft(n)', globals=globals(), number=10000), end='\n\n')

