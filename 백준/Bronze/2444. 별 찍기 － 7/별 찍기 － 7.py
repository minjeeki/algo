N = int(input())

star = 1
for i in range(N - 1):
    print(f"{' ' * (N - i - 1)}{'*' * star}")
    star += 2
for i in range(N):
    print(f"{' ' * (i)}{'*' * star}", end='')
    if i != N - 1:
        print(' ')
    else:
        print()
    star -= 2