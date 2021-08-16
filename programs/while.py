import os
import time

def eat_loop():
    cs = os.get_terminal_size().columns
    counter = 0
    while True:
        s = ' 猫 吃 鼠'
        slen = 9  # s 的长度
        if counter <= (cs-slen):
            print('\b' * (slen - 1) + s, end='', flush=True)
        else:
            back = '\b' * (slen + 1)
            print(back + s + '\b', end='', flush=True)
        if counter >= (cs-slen)*2:
            counter = 0
        counter += 1
        time.sleep(0.1)


def sum_numbers(to=100):
    total = 0
    n = 1
    while n <= to:
        total += n
        n += 1
    print(F'累加 1-{to} 的总和是 {total}')


if __name__ == '__main__':
    # eat_loop()
    sum_numbers(100)
