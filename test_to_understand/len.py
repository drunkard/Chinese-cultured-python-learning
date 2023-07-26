#!/usr/bin/python3


def len_by_cursor(strings):
    """字符串长度：英文字母按1个，汉字算2个"""
    length = 0
    for s in strings:
        if ord(s) > 127:
            length += 1
        else:
            length += 2
    return length
