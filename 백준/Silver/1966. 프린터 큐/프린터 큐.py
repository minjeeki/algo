T = int(input())
for tc in range(1, T+1):
    # 1. 전처리
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    value_M = queue[M]
    queue[M] = -1
    # 2. 동작 - value_M이 최고 우선순위의 값일 때
    if value_M == max(queue):
        cnt = 0
        for i in range(M + 1):
            if queue[i] == value_M:
                cnt += 1
        print(cnt + 1)
    # 2. 동작 - 9부터 value_M까지 반복문 돌며 시뮬레이션 진행
    else:
        total_cnt = 0
        # print(queue)
        # value_M 직전까지 계산
        for priority in range(9, value_M, -1):
            while priority in queue:
                idx_p = queue.index(priority)
                queue = queue[idx_p + 1:] + queue[:idx_p]
                total_cnt += 1
        # print(queue, total_cnt)
		# value_M에 대해서 -1 도달 전까지 cnt
        idx = 0
        while queue[idx] != -1:
            if queue[idx] == value_M:
                total_cnt += 1
            idx += 1
        print(total_cnt + 1)