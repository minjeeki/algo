N = int(input())

for i in range(1, N + 1):
    print(f"{'*' * i}{' ' * (N - i)}{' ' * (N - i)}{'*' * i}")
for j in range(N - 1, 0, -1):
    print(f"{'*' * j}{' ' * (N - j)}{' ' * (N - j)}{'*' * j}")