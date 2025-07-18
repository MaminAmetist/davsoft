"""
14. Дан текстовый файл, в каждой строке которого находится наименование месяца и сумма,
разделитель - точка с запятой. Подсчитать сколько раз в течение года сумма уменьшается
и увеличивается в текущем месяце по сравнению с предыдущим. Учесть, месяцы в файле могут
идти не по порядку их следования в течение года.
"""

month_dict = {
    'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4,
    'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
    'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}

lst = []
with open('task_14_file_14.txt', 'r', encoding='utf-8') as file:
    for line in file:
        month, count = line.strip().split(';')
        lst.append((month_dict[month], float(count)))

lst.sort()

increase = decrease = 0
for i in range(1, len(lst)):
    prev = lst[i - 1][1]
    curr = lst[i][1]
    if curr > prev:
        increase += 1
    elif curr < prev:
        decrease += 1

print(f'Сумма увеличивалась: {increase} раз')
print(f'Сумма уменьшалась: {decrease} раз')
