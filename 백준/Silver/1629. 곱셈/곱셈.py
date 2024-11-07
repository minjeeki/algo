def split_think(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (split_think(a, b // 2, c) ** 2) % c
    else:
        return ((split_think(a, b // 2, c) ** 2 ) * a ) % c

a, b, c = map(int, input().split())
print(split_think(a, b, c))