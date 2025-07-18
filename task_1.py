"""
1. Заполнить массив (100 элементов) случайными значениями (целое беззнаковое).
Найти максимальный и минимальный элемент массива и их индексы, вывести на экран.
"""

from random import randint

lst = [randint(1, 1000) for i in range(0, 100)]
max_elem, min_elem = max(lst), min(lst)
index_max_elem = lst.index(max_elem)
index_min_elem = lst.index(min_elem)

print(f'Максимальный элемент: {max_elem}\n'
      f'Минимальный элемент: {min_elem}\n'
      f'Индекс максимального элемента: {index_max_elem}\n'
      f'Индекс минимального элемента: {index_min_elem}')
