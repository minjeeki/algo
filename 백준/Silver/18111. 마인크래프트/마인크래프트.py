N, M, B = map(int, input().split())     # N : 세로, M : 가로, B : 블록 개수
place = []
sum_place = 0
for _ in range(N):
    cur_lst = list(map(int, input().split()))
    place += cur_lst
    sum_place += sum(cur_lst)
min_time = 256 * N * M
that_height = 0
for hi in range(min(place), max(place) + 1):
    # 인벤토리 포함 전체 블록 수가 hi로 평탄화 후 블록 수보다 작으면 고려 안함
    if (hi * N * M) > (B + sum_place):
        continue
    time = 0
    for i in range(N * M):
        # 블록이 목표 높이와 동일 : 다음 반복문 진행
        if place[i] == hi:
            continue
        # 블록 꺼내 인벤 넣기 : 2초 소요
        elif place[i] > hi:
            time += (place[i] - hi) * 2
        # 인벤에서 블록 꺼내 쌓기 : 1초 소요
        elif place[i] < hi:
            time += (hi - place[i])
    # 최소 시간 발견 : 시간 및 높이 갱신
    if time < min_time:
        min_time = time
        that_height = hi
    # 최소 시간과 동일 상황 발생 : 최대 높이 갱신
    elif time == min_time:
        that_height = max(that_height, hi)
print(min_time, that_height)