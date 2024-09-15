import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(10 ** 6)
# print(sys.getrecursionlimit())
input = sys.stdin.readline

def ft_dfs(point):
    global visited

    for next in near_lst[point]:
        if next not in visited:
            visited.add(next)
            ft_dfs(next)
    else:
        return

N, M = map(int, input().split())
near_lst = [[] for _ in range(N + 1)]
near_lst[0] = None
visited = set()
for _ in range(M):
    u, v = map(int, input().split())
    near_lst[u].append(v)
    near_lst[v].append(u)

result = 0
for start_idx in range(1, N + 1):
    if len(visited) == N:
        break
    if start_idx not in visited:
        result += 1
        visited.add(start_idx)
        ft_dfs(start_idx)
print(result)