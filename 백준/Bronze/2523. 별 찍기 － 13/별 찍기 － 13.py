N = int(input())

for i in range(1, N + 1):
    print(f"{'*' * i} ")
for j in range(N - 1, 0, -1):
    print(f"{'*' * j}", end='')
    if j != 1:
        print(' ')
    else:
        print()