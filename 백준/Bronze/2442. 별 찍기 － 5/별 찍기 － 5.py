N = int(input())

star = 1
for i in range(N):
    print(f"{' ' * (N - i - 1)}{'*' * star}", end='')
    if i != N - 1:
        print(' ')
    else:
        print()
    star += 2