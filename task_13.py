"""
13. Дан текстовый файл, в каждой строке которого находится наименование товара, цена
(точность два знака после запятой, разделитель дробной и целой части точка), и количество
(точность 3 знака после запятой), разделитель - точка с запятой. Вывести в файл наименование
товара, цену, количество и сумму (через точку с запятой). Также в файл вывести ИТОГО по
количеству и сумме.
"""

with (open('task_13_1_file_13_1.txt', 'r', encoding='utf-8') as infile,
      open('task_13_2_file_13_2.txt', 'w', encoding='utf-8') as outfile):
    lst = infile.read().split()
    total_price, total_count = 0, 0
    for string in lst:
        string = string.split(';')
        name = string[0]
        price = float(string[1])
        count = float(string[2])
        summ = price * count
        total_price += price
        total_count += count
        outfile.write(f'{name};{price};{count};{summ}\n')
    outfile.write(f'ИТОГО;{round(total_price, 2)};{round(total_count, 3)};'
                  f'{total_count * total_price}')
