import time

# chars = ''
start, distance = 97, 26
counter = distance

def loop():
    global counter
    for n in range(start, start + distance):
        counter -= 1
        c = chr(n)
        # chars += c
        # print(f'counter = {counter}')  # debug
        if counter > 0:
            print(c, end='', flush=True)
        else:
            # print('\b', end='', flush=True)
            print('\b\033[K\033[0m', end='', flush=True)
            if abs(counter) >= distance:
                counter = distance
        time.sleep(0.1)

for _ in range(7):
    loop()

print()
