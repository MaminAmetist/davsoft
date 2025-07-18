"""
2. Заполнить массив (100 элементов) случайными значениями (целое беззнаковое).
Найти количество элементов в диапазоне 0-10,11-100,101-1000 и т.д. до 1_000_001, числа свыше
считать отдельно. Вывести на экран.
"""

from random import randint
from functools import reduce

lst = [randint(1, 10_000_000) for i in range(0, 100)]

count_0_10, count_11_100, count_101_1000, count_1001_10000 = 0, 0, 0, 0
for elem in lst:
    if elem <= 10:
        count_0_10 += 1
    elif elem <= 100:
        count_11_100 += 1
    elif elem <= 1000:
        count_101_1000 += 1
    elif elem <= 10_000:
        count_1001_10000 += 1
        ...

count_10001_100000 = len([elem for elem in lst if 10_000 < elem <= 100_000])

count_100001_1000000 = sum(map(lambda elem: elem in range(100_001, 1_000_001), lst))

count_1_000_001 = reduce(lambda count, elem: count + (elem > 1_000_000), lst, 0)

print(count_0_10)
print(count_11_100)
print(count_101_1000)
print(count_1001_10000)
print(count_10001_100000)
print(count_100001_1000000)
print(count_1_000_001)
