import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
index = 1

for _ in range(T):
    N, K = map(int, data[index].split())
    build_time = [0] + list(map(int, data[index + 1].split()))
    build_near_lst = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    
    index += 2
    for i in range(K):
        x, y = map(int, data[index].split())
        build_near_lst[x].append(y)
        in_degree[y] += 1
        index += 1

    W = int(data[index])
    index += 1
    
    # 위상 정렬
    times = build_time[:]
    deq = deque()

    # 진입 차수가 0인 노드를 먼저 큐에 넣음
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            deq.append(i)

    while deq:
        now = deq.popleft()
        for next_building in build_near_lst[now]:
            in_degree[next_building] -= 1
            times[next_building] = max(times[next_building], times[now] + build_time[next_building])
            if in_degree[next_building] == 0:
                deq.append(next_building)

    print(times[W])
