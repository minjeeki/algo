N_lst = list(input())
if sum(list(map(int, N_lst))) % 3 == 0 and '0' in N_lst:
    print(''.join(sorted(N_lst, reverse=True)))
else:
    print(-1)