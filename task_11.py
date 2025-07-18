"""
11. Дан текстовый файл. Необходимо обработать каждое слово - первую букву сделать заглавной,
а остальные - строчными. Результат записать в другой файл.
"""

with (open('task_11_1_file_11_1.txt', 'r', encoding='utf-8') as infile,
      open('task_11_2_file_11_2.txt', 'w', encoding='utf-8') as outfile):
    for line in infile:
        text_lst = line.split('\n')
        title_text_lst = [word.title() for word in text_lst]
        outfile.write(' '.join(title_text_lst))
