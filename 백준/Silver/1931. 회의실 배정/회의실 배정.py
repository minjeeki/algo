N = int(input())

# 입력값 받기 & 정렬
time_table = [list(map(int, input().split())) for _ in range(N)]
# print(time_table)
time_table.sort(key=lambda x: (-x[1], -x[0]))
# print(time_table)

# 뒤에서부터 접근하며, 그리디 & total_cnt 세기
total_cnt = 1
cur_time = time_table[0]
for time1 in time_table[1:]:
    # cur_time의 s_time보다 time1의 e_time이 큼 (cur_time과 겹쳐진 상황)
    if cur_time[0] < time1[1] and cur_time[0] < time1[0]:
        cur_time = time1
        # print(time1, 'cur_time switch')
    # time1의 e_time이 cur_time의 s_time보다 작거나 같을 경우
    elif time1[1] <= cur_time[0] and time1[1] <= cur_time[1]:
        cur_time = time1
        total_cnt += 1
        # print(time1, 'total_cnt +!')
    # else:
        # print(time1, cur_time, 'nothing')
print(total_cnt)