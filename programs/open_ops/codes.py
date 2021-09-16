#!/usr/bin/python3

# 文本编码
# gb2312 < gbk < gb18030
with open('gb18030', 'w', encoding='GB18030') as f:
    f.write('天对地，雨对风，大陆对长空\n')
    f.write('龘\n')

with open('gb2312', 'w', encoding='GB2312') as f:
    f.write('天对地，雨对风，大陆对长空\n')
    # f.write('龘\n')

with open('gbk', 'w', encoding='GBK') as f:
    f.write('天对地，雨对风，大陆对长空\n')
    f.write('龘\n')

with open('utf8', 'w', encoding='UTF-8') as f:
    f.write('天对地，雨对风，大陆对长空\n')
    f.write('龘\n')
