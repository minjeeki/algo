N, r, c = map(int, input().split())

def find_num(N, r, c):
    num = 0
    size = 2 ** N
    while size > 1:
        size //= 2
        row, col = r // size, c // size
        num += size ** 2 * (row * 2 + col)
        r %= size
        c %= size
    if r == 0 and c == 0:
        return num
    elif r == 0 and c == 1:
        return num + 1
    elif r == 1 and c == 0:
        return num + 2
    else:
        return num + 3

print(find_num(N, r, c))