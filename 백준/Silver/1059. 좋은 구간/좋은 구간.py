L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

idx = 0
start = 1
end = 1
has_same_num = False
while idx < L:
    if S[idx] < n:
        start = S[idx] + 1
        idx += 1
    elif S[idx] == n:
        has_same_num = True
        break
    elif S[idx] > n:
        end = S[idx] - 1
        break
if has_same_num:
    print(0)
else:
    print((n - start + 1) * (end - n + 1) - 1)