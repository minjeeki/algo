def dfs(point):
    global visited

    visited[point] = True
    for next in near_lst[point]:
        if visited[next] == False:
            dfs(next)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    near_lst = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        p1, p2 = map(int, input().split())
        near_lst[p1].append(p2)
        near_lst[p2].append(p1)
    cnt = 0
    for idx in range(1, N+1):
        if visited[idx] == False:
            cnt += 1
            dfs(idx)
    print(f'#{tc} {cnt}')