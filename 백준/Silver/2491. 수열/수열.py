N = int(input())
n_lst = list(map(int, input().split()))
max_len = 0
# 오름차순에서 최대 길이 구하기
now_len = 1
for idx in range(N - 1):
    if n_lst[idx + 1] >= n_lst[idx]:
        now_len += 1
    else:
        max_len = max(max_len, now_len)
        now_len = 1
max_len = max(max_len, now_len)
# 내림차순에서 최대 길이 구하기
now_len = 1
for idx in range(N - 1):
    if n_lst[idx + 1] <= n_lst[idx]:
        now_len += 1
    else:
        max_len = max(max_len, now_len)
        now_len = 1
max_len = max(max_len, now_len)
print(max_len)