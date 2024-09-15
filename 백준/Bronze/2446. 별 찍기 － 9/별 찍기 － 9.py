N = int(input())

star = 2 * N - 1
for i in range(N):
    print(f"{' ' * (i)}{'*' * star} ")
    star -= 2
star = 3
for i in range(1, N):
    print(f"{' ' * (N - i - 1)}{'*' * star} ")
    star += 2