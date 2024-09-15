N = int(input())

star = 2 * N - 1
for i in range(N):
    print(f"{' ' * (i)}{'*' * star}", end='')
    if i != N - 1:
        print(' ')
    else:
        print()
    star -= 2