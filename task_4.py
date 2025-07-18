"""
4. Заполнить массив (100 элементов) случайными целыми значениями со знаком.
Создать два массива, один из которых заполнить положительными, а другой отрицательными
значениями из первого массива.
"""

from random import randint

lst = [randint(-10, 10) for elem in range(1, 101) if elem != 0]

lst_positive = [el for el in lst if el > 0]
lst_negative = [el for el in lst if el < 0]
