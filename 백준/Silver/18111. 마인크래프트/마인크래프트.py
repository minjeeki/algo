N, M, B = map(int, input().split())     # N : 세로, M : 가로, B : 블록 개수
place = []
for _ in range(N):
    place += list(map(int, input().split()))
sum_place = sum(place)
min_time = 256 * N * M
that_height = 0
for hi in range(min(place), max(place) + 1):
    if (hi * N * M) > (B + sum_place):
        continue
    time = 0
    inven = B
    for i in range(N * M):
        if place[i] == hi:
            pass
        # 블록 꺼내 인벤 넣기 : 2초 소요
        elif place[i] > hi:
            time += (place[i] - hi) * 2
        # 인벤에서 블록 꺼내 쌓기 : 1초 소요
        elif place[i] < hi:
            time += (hi - place[i])
    if time < min_time:
        min_time = min(time, min_time)
        that_height = hi
    elif time == min_time:
        that_height = max(that_height, hi)
print(min_time, that_height)