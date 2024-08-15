S = input()
alp_lst = [-1] * (ord('z') - ord('a') + 1)
for idx in range(len(S)):
    alp_idx = ord(S[idx]) - ord('a')
    if alp_lst[alp_idx] == -1:
        alp_lst[alp_idx] = idx
print(*alp_lst)