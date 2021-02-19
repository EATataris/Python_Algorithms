"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time, sys

def list_fill(n):
    start_val = time.time()
    lst = [i for i in range(n)]
    end_val = time.time()

    return lst, end_val - start_val


def dict_fill(n):
    start_val = time.time()
    dct = {key: key for key in range(n)}
    end_val = time.time()
    return dct, end_val - start_val


lst1 = list_fill(10000000)[0]
dct1 = dict_fill(10000000)[0]


def list_clear(lst):
    start_val = time.time()
    lst1.clear()
    end_val = time.time()
    return lst, end_val - start_val


def dict_clear(dct):
    start_val = time.time()
    dct.clear()
    end_val = time.time()
    return dct, end_val - start_val


print(sys.getsizeof(lst1))
print(sys.getsizeof(dct1))

print(f'Операция заполнения списка заняла {list_fill(10000000)[1]} сек')
print(f'Операция заполнения словаря заняла {dict_fill(10000000)[1]} сек')
# Вывод: наполнение списка выполняется быстрее, нежели наполнение словаря при прочих равных условиях. Из-за того, что список потребляет
# приблизительно в 5 раз меньше памяти, что мы можем вижеть при помощи функции getsizeof
print(f'Операция удаления эл-та списка заняла {list_clear(lst1)[1]} сек')
print(f'Операция удаления эт-то словаря заняла {dict_clear(dct1)[1]} сек')
# Вывод: очистка списка происходит немного, но быстрее нежели очистка словаря по той же причине потребления большего кол-ва памяти списком.


def decorator(func):
    def wrapper(n):
        start_val = time.time()
        wrap = func(n)
        end_val = time.time()
        print(f'Операция заняла {end_val - start_val} сек')
        return wrap
    return wrapper


@decorator
def list_fill(n):
    lst = [i for i in range(n)]
    return lst


@decorator
def dict_fill(n):
    dct = {key: key for key in range(n)}
    return dct


@decorator
def list_clear(lst):
    lst1.clear()
    return lst


@decorator
def dict_clear(dct):
    dct.clear()
    return dct1


list_fill(10000000)
dict_fill(10000000)
list_clear(lst1)
dict_clear(dct1)