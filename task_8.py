"""
8. Дан текстовый файл. Подсчитать отношение количества встречающихся в файле гласных буквы
русского алфавита (для каждой буквы отдельно) к общему количеству символов в файле.
Результат вывести (букву и отношение) на экран в порядке убывания.
"""

count_dict = {'а': 0, 'е': 0, 'ё': 0, 'и': 0, 'о': 0, 'у': 0, 'э': 0, 'ю': 0, 'я': 0}

with open('task_8_file_8.txt', 'r', encoding='utf-8') as file:
    lst = list(file.read().lower())
    for key, value in count_dict.items():
        count_dict[key] = lst.count(key) / len(lst)

sorted_count_dict = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

for key, value in sorted_count_dict:
    print(key, value)
