candi = ['ascending', 'descending', 'mixed']
candi_idx = 2
num_lst = list(map(int, input().split()))
if num_lst[0] == 1:
    candi_idx = 0
    for idx in range(1, 7):
        if num_lst[idx] != idx + 1:
            candi_idx = 2
            break
elif num_lst[0] == 8:
    candi_idx = 1
    for idx in range(1, 7):
        if num_lst[idx] != 8 - idx:
            candi_idx = 2
            break
else:
    candi_idx = 2
print(candi[candi_idx])