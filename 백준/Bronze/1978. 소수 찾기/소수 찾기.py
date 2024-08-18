N = int(input())
n_lst = list(map(int, input().split()))
cnt = 0
for n in n_lst:
    is_sosu = 0
    for i in range(n + 1):
        if i != 0 and n % i == 0:
            is_sosu += 1
    if is_sosu == 2:
        cnt += 1
print(cnt)