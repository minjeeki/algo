import sys

def ft_dfs(x):
    global cnt, min_cnt
    if cnt > min_cnt:
        return
    if x == 1:
        min_cnt = min(cnt, min_cnt)
        return
    if x % 3 == 0:
        cnt += 1
        ft_dfs(x // 3)
        cnt -= 1
    if x % 2 == 0:
        cnt += 1
        ft_dfs(x // 2)
        cnt -= 1
    cnt += 1
    ft_dfs(x - 1)
    cnt -= 1

X = int(input())

cnt = 0
min_cnt = sys.maxsize
ft_dfs(X)
print(min_cnt)