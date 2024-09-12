import sys

def ft_dfs(x):
    global cnt, min_cnt, steps,final_step
    # 가지치기
    if cnt > min_cnt:
        return
    # 재귀 : 기저 조건 (종료 조건)
    if x == 1 and cnt < min_cnt:
        min_cnt = cnt
        final_step = ' '.join(list(map(str, steps)))
        return
    # 함수 더 나아가기
    if x % 3 == 0:
        cnt += 1
        steps.append(x // 3)
        ft_dfs(x // 3)
        steps.pop()
        cnt -= 1
    if x % 2 == 0:
        cnt += 1
        steps.append(x // 2)
        ft_dfs(x // 2)
        steps.pop()
        cnt -= 1
    cnt += 1
    steps.append(x - 1)
    ft_dfs(x - 1)
    steps.pop()
    cnt -= 1

X = int(input())

cnt = 0
min_cnt = sys.maxsize
steps = [X]
final_step = ''
ft_dfs(X)
print(min_cnt)
print(final_step)