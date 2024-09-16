def ft_dfs(num, chonsu):
    global visited

    # 가지치기
    if chonsu >= 2:
        return
    for next_num in near_lst[num]:
        # print(num, next_num)
        visited.add(next_num)
        ft_dfs(next_num, chonsu + 1)

N = int(input())
M = int(input())
near_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    near_lst[a].append(b)
    near_lst[b].append(a)

sangun = 1
visited = set()
visited.add(sangun)
ft_dfs(sangun, 0)
# print(*list(visited))
print(len(visited) - 1)