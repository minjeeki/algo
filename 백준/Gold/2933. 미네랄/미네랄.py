from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def throw_stick(cave, R, C, height, from_left):
    row = R - height
    cols = range(C) if from_left else reversed(range(C))
    for col in cols:
        if cave[row][col] == 'x':
            cave[row][col] = '.'
            return (row, col)
    return None

def mark_ground_cluster(cave, R, C):
    visited = [[False] * C for _ in range(R)]
    queue = deque()

    for col in range(C):
        if cave[R-1][col] == 'x' and not visited[R-1][col]:
            visited[R-1][col] = True
            queue.append((R-1, col))

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
    return visited

def find_floating_cluster(cave, visited, R, C, start):
    r, c = start
    if not (0 <= r < R and 0 <= c < C) or cave[r][c] != 'x' or visited[r][c]:
        return None

    cluster = []
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    cluster.append((r, c))
    cave[r][c] = '.'

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
                cluster.append((nr, nc))
                cave[nr][nc] = '.'  # 일단 삭제
    return cluster

def compute_fall_distance(cave, cluster, R, C, visited):
    cluster_set = set(cluster)
    min_dist = R
    for r, c in cluster:
        nr = r + 1
        dist = 0
        while nr < R:
            if cave[nr][c] == 'x' and visited[nr][c]:
                break
            if (nr, c) in cluster_set:
                nr += 1
                continue
            if cave[nr][c] == 'x':
                break
            dist += 1
            nr += 1
        min_dist = min(min_dist, dist)
    return min_dist

def apply_fall(cave, cluster, fall_distance):
    for r, c in sorted(cluster, reverse=True):
        cave[r + fall_distance][c] = 'x'

def handle_cluster_fall(cave, R, C, broken_pos):
    visited = mark_ground_cluster(cave, R, C)

    for d in range(4):
        nr, nc = broken_pos[0] + dr[d], broken_pos[1] + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if cave[nr][nc] == 'x' and not visited[nr][nc]:
                floating_cluster = find_floating_cluster(cave, visited, R, C, (nr, nc))
                if floating_cluster:
                    fall_dist = compute_fall_distance(cave, floating_cluster, R, C, visited)
                    apply_fall(cave, floating_cluster, fall_dist)
                break

R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
throws = list(map(int, input().split()))

for i in range(N):
    height = throws[i]
    from_left = (i % 2 == 0)
    broken = throw_stick(cave, R, C, height, from_left)
    if broken:
        handle_cluster_fall(cave, R, C, broken)

for row in cave:
    print(''.join(row))
