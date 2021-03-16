"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

companies = {'apple': 4000, 'samsung': 5000, 'google': 6000, 'amazon': 7000, 'tesla': 8000}


def max_income_one(comp): # O(n log n)
    return sorted(comp.items(), key=lambda x: x[1], reverse=True)[:3]

print(max_income_one(companies))

def max_income_two(comp): # O(n)
    lst = []
    new_d = dict(comp)
    for i in range(3):
        max_inc = max(new_d, key=new_d.get)
        del new_d[max_inc]
        lst.append(max_inc)
    return lst

print(max_income_two(companies))

# Вывод: второе решение лучше, потому что сложность линейная. А она по всем параметрам продуктивнее
# чем линейно-логарифимеческая как в первом решении