def ft_dfs(start_p, depth):
    global chonsu, visited
    # 기저 조건
    if start_p == p2:
        chonsu = depth
        return
    for next_p in near_lst[start_p]:
        if next_p not in visited:
            visited.add(next_p)
            ft_dfs(next_p, depth + 1)
            visited.remove(next_p)


N = int(input())
p1, p2 = map(int, input().split())
M = int(input())

near_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    near_lst[x].append(y)
    near_lst[y].append(x)
chonsu = -1
visited = set()
ft_dfs(p1, 0)
print(chonsu)