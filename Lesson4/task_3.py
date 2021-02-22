"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return str(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return str(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


n = 12345


def main():
    revers_1(n)
    revers_2(n)
    revers_3(n)
    revers_4(n)


print(timeit('revers_1(n)', globals=globals(), number=1000))
print(timeit('revers_2(n)', globals=globals(), number=1000))
print(timeit('revers_3(n)', globals=globals(), number=1000))
print(timeit('revers_4(n)', globals=globals(), number=1000))
run('main()')

'''
Вывод реализацие через срез строки через обратный шаг наиболее предпочтительная так как застрачивает меньше всего
времени. Реализация через функцию reverced тоже хорошо по быстродействию, но проигрывает в это плане срезу.
'''