from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * N for _ in range(N)]

for start in range(N):
    visited = [False] * N
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for next_node in range(N):
            if graph[cur][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    for i in range(N):
        if visited[i]:
            result[start][i] = 1

for row in result:
    print(*row)
