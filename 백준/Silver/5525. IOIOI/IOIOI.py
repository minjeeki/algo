N = int(input())
M = int(input())
S = input()

PN = 'IO' * N + 'I'
len_pn = len(PN)
cnt = 0
for idx in range(M):
    if (idx + len_pn) <= M and S[idx] == 'I' \
        and S[idx + len_pn - 1] == 'I' and S[idx:idx + len_pn] == PN:
        cnt += 1
print(cnt)