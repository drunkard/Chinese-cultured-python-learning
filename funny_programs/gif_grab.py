#!/usr/bin/python3
import os
import re
import requests
import sys
import urllib


portal_url = 'http://qq.yh31.com/ql/ls/'
dst_dir = os.path.expanduser('~/gifs')
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir, mode=755)
elif os.path.exists(dst_dir) and not os.path.isdir(dst_dir):
    print(F'文件已存在，且不是目录，请更改变量： dst_dir = {dst_dir}')
    sys.exit()

# 提取URL主机部分
_us = urllib.parse.urlparse(portal_url)
base_url = ''.join([_us.scheme, '://', _us.netloc])
# print(F'base_url = {base_url}')  # debug


#获取url_list,就是所有的图片链接
def get_url(url):
    "提取页面上的所有图片 URL"
    response = requests.get(url)
    response.encoding='utf-8'  # 设置页面编码，否则是乱码
    url_addr = r'<img src=".*?" data-src="(.*?)" alt="(.*?)" border="0"/>'  # 提取图片URL的正则表达式规则
    url_list = re.findall(url_addr, response.text)  # 开始提取
    return url_list


#下载保存所有的图片
def get_gif(url, fname):
    response = requests.get(url)
    with open(dst_dir + F"/{fname}.gif", 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_list = get_url(portal_url)
    sn = 1
    for url, name in url_list:
        url = base_url + url
        name = name or sn  # if name is empty, use 'sn' instead
        print(F'{url} -> {name}')  # debug
        get_gif(url, name)
        sn += 1
