N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[0], x[1]))
# print(meetings)
cnt = 0
can_use = True
cur_meeting = []
for meeting in meetings:
    if can_use:
        cur_meeting = meeting
        can_use = False
        cnt += 1
    else:
        # 현재 끝나는 시간이 다음 시작 시간보다 빠름
        if cur_meeting[1] <= meeting[0]:
            cur_meeting = meeting
            cnt += 1
        # 현재 끝나는 시간이 다음 끝나는 시간보다 빠름
        elif cur_meeting[1] <= meeting[1]:
            continue
        # 현재 끝나는 시간이 다음 끝나는 시간보다 느림
        elif cur_meeting[1] > meeting[1]:
            cur_meeting = meeting
print(cnt)
