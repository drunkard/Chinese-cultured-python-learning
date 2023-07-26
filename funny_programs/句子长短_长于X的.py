import sys


def longer_than(sentences, length):
    splits = ['。', '！', '？']  # 句子分隔符
    for split in splits:
        sentences = [s.split(split) for s in sentences]
        sentences = [y for x in sentences for y in x]  # unfold list of list
    return [s for s in sentences if len(s) > length]


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        file_name = sys.argv[1]
        length = int(sys.argv[2])
    else:
        print(f'用法： {sys.argv[0]} <文件名> <句子的最低字数>')
        sys.exit()

    with open(file_name, 'r') as f:
        ss = longer_than(f.readlines(), length)
        print(f'字数大于 {length} 的句子有 {len(ss)} 个')
        print(ss)
