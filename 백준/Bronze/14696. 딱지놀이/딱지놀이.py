N = int(input())
for round in range(N):
    # 입력값 처리
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_cnt = [0] * 5
    b_cnt = [0] * 5
    for i in range(1, a[0] + 1):
        a_cnt[a[i]] += 1
    for i in range(1, b[0] + 1):
        b_cnt[b[i]] += 1
    # print(a_cnt, b_cnt)
    # 라운드 비교
    for cnt in range(4, 0, -1):
        if a_cnt[cnt] > b_cnt[cnt]:
            print('A')
            break
        elif a_cnt[cnt] < b_cnt[cnt]:
            print('B')
            break
    else:
        print('D')