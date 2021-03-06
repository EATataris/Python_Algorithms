"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


num = int(input('Введите число элементов: '))
orig_list = [random.uniform(0, 50) for _ in range(num)]
print(f'исходный массив {orig_list}')
print(f'отсортированнй {merge_sort(orig_list)}')

print(timeit.timeit('merge_sort(orig_list[:])', globals=globals(), number=1000))


def merge_sort_two(lst_obj):
    n = len(lst_obj)
    if n < 2:
        return lst_obj

    center = n // 2
    left = merge_sort_two(lst_obj[:center])
    right = merge_sort_two(lst_obj[center:n])

    i = j = 0
    sorted_lst = []
    while i < len(left) or j < len(left):
        if not i < len(left):
            sorted_lst.append(right[j])
            j += 1
        elif not j < len(right):
            sorted_lst.append(left[i])
            i += 1
        elif left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1
    return sorted_lst


orig_list_two = [random.uniform(0, 50) for _ in range(num)]
print(f'исходный массив {orig_list_two}')
print(f'отсортированнй {merge_sort_two(orig_list_two)}')

print(timeit.timeit('merge_sort_two(orig_list_two[:])', globals=globals(), number=1000))