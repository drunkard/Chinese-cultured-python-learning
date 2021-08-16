import time

sleep = 0.05

def xx():
    for n in range(97, 97+26):
        print(chr(n), end='', flush=True)
        time.sleep(sleep)
    for n in range(97, 123):
        print('\b \b', end='', flush=True)
        time.sleep(sleep)

for _ in range(9):
    xx()
