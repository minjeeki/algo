N_switch = int(input())
status = [-1] + list(map(int, input().split()))
M_student = int(input())
for _ in range(M_student):
    sex, num_switch = map(int, input().split())
    if sex == 1:
        idx_change = num_switch
        while idx_change < N_switch + 1:
            status[idx_change] = 0 if status[idx_change] == 1 else 1
            idx_change += num_switch
    if sex == 2:
        status[num_switch] = 0 if status[num_switch] == 1 else 1
        idx_before = num_switch - 1
        idx_after = num_switch + 1
        while idx_before >= 1 and idx_after < N_switch + 1:
            if status[idx_before] == status[idx_after]:
                status[idx_before] = 0 if status[idx_before] == 1 else 1
                status[idx_after] = 0 if status[idx_after] == 1 else 1
                idx_before -= 1
                idx_after += 1
            else:
                break
idx = 1
while idx < (N_switch + 1):
    if idx + 20 > N_switch + 1:
        print(*status[idx:])
    else:
        print(*status[idx:idx + 20])
    idx += 20