from collections import deque
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def ft_bfs(cur_x, cur_y):
    result = 0
    visited = set()
    visited.add((cur_x, cur_y))
    deq = deque()
    deq.append((cur_x, cur_y))
    while deq:
        cx, cy = deq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and \
                matrix[nx][ny] != 'X' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    deq.append((nx, ny))
                    if matrix[nx][ny] == 'P':
                        result += 1
    if result == 0:
        result = 'TT'
    return result

N, M = map(int, input().split())
matrix = [0] * N
cur_x = -1
cur_y = -1
for idx in range(N):
    matrix[idx] = list(input())
    if cur_x == -1:
        for jdx in range(M):
            if matrix[idx][jdx] == 'I':
                cur_x = idx
                cur_y = jdx
                break
cnt_person = ft_bfs(cur_x, cur_y)
print(cnt_person)
