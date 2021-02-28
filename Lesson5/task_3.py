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

x = 100
print(timeit('list_append(x)', globals=globals(), number=1000))
print(timeit('deque_list_append(x)', globals=globals(), number=1000))

print(timeit('list_pop()', globals=globals(), number=10000))
print(timeit('deque_list_pop()', globals=globals(), number=10000))

print(timeit('list_remove()', globals=globals(), number=10000))
print(timeit('deque_list_pop_left()', globals=globals(), number=10000))

