from collections import deque

T = int(input())
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

for _ in range(T):
    # 입력값 받기
    N, M, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    # print(*matrix)
    # 배추 덩어리 개수 세기
    cnt = 0
    for idx in range(N):
        for jdx in range(M):
            if matrix[idx][jdx] == 1:
                matrix[idx][jdx] = -1
                deq = deque()
                deq.append([idx, jdx])
                cnt += 1
                while len(deq) > 0:
                    cx, cy = deq.popleft()
                    for di in directions:
                        nx = cx + di[0]
                        ny = cy + di[1]
                        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                            matrix[nx][ny] = -1
                            deq.append([nx, ny])
    print(cnt)
                
                
