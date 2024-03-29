#!/cc/bin/python3
'''
打印加法表:
    高亮记忆技巧；
    高亮变化的数字；
'''
from termcolor import colored, cprint

cprint('加法表：', color='cyan')
for l in range(0, 11):
    for r in range(0, 11):
        if l+r > 10:
            break
        cl = colored(l, color='green', attrs=['blink'])
        csum = colored(l+r, color='cyan', attrs=['blink'])
        print(f'{cl}+{r}={csum}\t', end='')
    print()


print()
cprint('减法表：', color='cyan')
for l in range(0, 11):
    for r in range(0, 11):
        if l < r:
            break
        cl = colored(l, color='green', attrs=['blink'])
        csum = colored(l-r, color='cyan', attrs=['blink'])
        print(f'{cl}-{r}={csum}\t', end='')
    print()
