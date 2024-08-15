left_lst = [0] * 42
dif_cnt = 0
for _ in range(10):
    left = int(input()) % 42
    if left_lst[left] == 0:
        dif_cnt += 1
        left_lst[left] = 1
print(dif_cnt)