for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j}x{i}={i*j}', end=' ') if i >= j else ''
    print()
