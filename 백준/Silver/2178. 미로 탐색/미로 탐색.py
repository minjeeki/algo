from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

N, M = map(int, input().split())

miro = [list(input()) for _ in range(N)]
# print(miro)
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
deq = deque()
deq.append((0, 0))
while deq:
    cx, cy = deq.popleft()
    if cx == N - 1 and cy == M - 1:
        print(visited[N - 1][M - 1])
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == '1' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[cx][cy] + 1
            deq.append((nx, ny))