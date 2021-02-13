"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class MyExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


class PlatesStack:
    def __init__(self, size):
        self.elems = []
        self.size = size

    def is_empty(self):
        return self.elems == []

    def is_full(self):
        return len(self.elems) == self.size

    def push_in(self, el):
        if len(self.elems) < self.size:
            self.elems.append(el)
        else:
            raise MyExeption('Создайте новый экземпляр класса')

    def pop_out(self):
        self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def show_stack(self):
        return self.elems


plates1 = PlatesStack(3)
plates1.push_in('plate')
plates1.push_in('plate')
plates1.push_in('plate')
# plates1.push_in('plate') - выдаст ошибку
plates2 = PlatesStack(4)
plates2.push_in('plate')
plates2.push_in('plate')