# 완전 탐색에서 100이 넘어가면 진행하기 부담스러움 (20부터도 부담스러움)

import sys

sys.setrecursionlimit(10 ** 6)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 상태 - row, col에서 끝까지 갔을 때 총 개수
def ft_backtracking(cx, cy):
    # 기저 조건
    if cx == M - 1 and cy == N - 1:
        # print('over')
        return 1
    # 이미 저장된 값 접근 시 저장된 값 이용
    if dp[cx][cy] != -1:
        # print(*dp, sep='\n')
        return dp[cx][cy]
    # 재귀
    dp[cx][cy] = 0
    # print('----', *dp, sep='\n')
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < M and 0 <= ny < N and matrix[cx][cy] > matrix[nx][ny]:
            dp[cx][cy] += ft_backtracking(nx, ny)

    return dp[cx][cy]

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
# print(*dp, sep='\n')
print(ft_backtracking(0, 0))