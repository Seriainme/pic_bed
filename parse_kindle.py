# coding:utf-8
import re
import random

'''
对于中文的笔记使用note代码块，random color 来展示。
英文的笔记用blockquote来展示
'''

alld = {}


def is_chinese(s):
    pattern = re.compile(r'[\u4e00-\u9fa5]')  # 匹配中文字符
    if pattern.search(s):
        return True
    else:
        return False


with open('clippings.txt', 'r', encoding='utf-8') as f:
    content = f.read()

clippings = content.split('==========')
for clipping in clippings:
    if not clipping.strip():
        continue
    lines = clipping.strip().split('\n')
    if len(lines) != 1:
        book_info = lines[0].strip().replace('\ufeff', '')
        book_info = '{% quot ' + book_info + ' %}  '
        content = lines[3].strip()
        alld.setdefault(book_info, []).append(content)

for k, v in alld.items():
    open('res.txt', 'a', encoding='utf-8').write('\n' + str(k) + '\n')
    filtered_list = list(filter(lambda x: not any(x in y for y in v if x != y), v))

    for content in filtered_list:
        if is_chinese(str(content)):
            color = random.choice(["orange", "yellow", "green", "cyan", "blue", "purple", "light", "warning"])
            content = '{% note color:' + f'{color} ' + content + ' %}'
        else:
            content = '> ' + content
        open('res.txt', 'a', encoding='utf-8').write('\n' + str(content) + '\n')
