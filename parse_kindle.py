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

        if is_chinese(str(content)[4:7]):
            color = random.choice(["orange", "yellow", "green", "cyan", "blue", "purple", "light", "warning"])
            content = '{% note color:' + f'{color} ' + content + ' %}'
        else:
            content = '> ' + content

        alld.setdefault(book_info, []).append(content)

for k, v in alld.items():
    open('res.txt', 'a', encoding='utf-8').write(str(k) + '\n')
    for one in v:
        open('res.txt', 'a', encoding='utf-8').write('\n' + str(one) + '\n')
