import time

start, distance = 97, 26
end = start + distance
counter = distance

sleep = 0.05

def eat_chars():
    '打印出字母，然后再吃掉'
    for n in range(97, 97+26):
        print(chr(n), end='', flush=True)
        time.sleep(sleep)
    for n in range(97, 123):
        print('\b \b', end='', flush=True)
        time.sleep(sleep)

def eat_chars_global_keyword():
    '学习 global 关键字用法'
    global counter
    for n in range(start, start + distance):
        counter -= 1
        c = chr(n)
        # print(f'counter = {counter}')  # debug
        if counter > 0:
            print(c, end='', flush=True)
        else:
            print('\b \b', end='', flush=True)
            if abs(counter) >= distance:
                counter = distance  # reset counter
        time.sleep(sleep)


if __name__ == '__main__':
    # print(eat_chars.__doc__)
    # for _ in range(9):
    #     eat_chars()

    for _ in range(9):
        eat_chars_global_keyword()
