board = [list(map(int, input().split())) for _ in range(5)]
call_num = []
for _ in range(5):
    call_num += list(map(int, input().split()))
cnt_bingo = 0
has_cross = 0
has_cross_x = 0
for idx in range(5 * 5):
    # 사회자가 읊은 숫자와 동일한 숫자가 있는 위치 찾기
    this_time = call_num[idx]
    check_i = -1
    check_j = -1
    for i in range(5):
        for j in range(5):
            if board[i][j] == this_time:
                board[i][j] = 0
                check_i = i
                check_j = j
                break
    # print(this_time, check_i, check_j)
    # 가로가 모두 빙고인지 확인
    if board[check_i].count(0) == 5:
        cnt_bingo += 1
    # 세로가 모두 빙고인지 확인
    is_bingo = True
    for c_idx in range(5):
        if board[c_idx][check_j] != 0:
            is_bingo = False
            break
    if is_bingo == True:
        cnt_bingo += 1
    # 대각선 빙고 존재 여부 확인
    if has_cross == 0 and check_i == check_j:
        is_bingo = True
        for cross_i in range(5):
            if board[cross_i][cross_i] != 0:
                is_bingo = False
                break
        if is_bingo == True:
            has_cross = 1
    # 역대각선 빙고 존재 여부 확인
    if has_cross_x == 0 and check_i + check_j == 4:
        is_bingo = True
        for cross_i in range(5):
            if board[cross_i][4 - cross_i] != 0:
                is_bingo = False
                break
        if is_bingo == True:
            has_cross_x = 1
    if (cnt_bingo + has_cross + has_cross_x) >= 3:
        print(idx + 1)
        break