"""
7. Дан текстовый файл, в каждой строке которого содержатся два числа с плавающей точкой.
Между собой разделены точкой с запятой. Проверить выполняется ли условие, что второе число
составляет 18% от первого.
"""
with open('task_7_file_7.txt', 'r') as file:
    for line in file:
        lst = line.strip().split(';')
        if round(float(lst[0]) * 0.18, 2) == float(lst[1]):
            print(line, 'ok')
        else:
            print(line, 'not ok')
