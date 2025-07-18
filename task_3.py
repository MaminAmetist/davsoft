"""
3. Заполнить массив целыми случайными значениями - 1 и 0. Определить отношение количества
единичек и нулей в массиве для 100,1000,10000 элементов. Вывести на экран.
"""

from random import randint

lst = [randint(0, 1) for _ in range(1, 101)]
print(sum(lst) / (len(lst) - sum(lst)))

lst = [randint(0, 1) for _ in range(1, 1001)]
count = 0
for elem in lst:
    if elem == 1:
        count += 1
print(count / (len(lst) - count))

lst = [randint(0, 1) for _ in range(1, 10_001)]
print(lst.count(1) / lst.count(0))
