"""
12. Дан текстовый файл с рассказом на русском языке. Проверить, является ли первая буква
каждого предложения заглавной. В случае несовпадения - вывести номер строки и слово,
написанное неверно.
"""

import re

with open('task_12_file_12.txt', 'r', encoding='utf-8') as file:
    text = re.split(r'[.\n!?—]+', file.read())
    for sent in text:
        if sent.lstrip(' ').islower():
            print(text.index(sent), sent.lstrip(' ').split()[0])
