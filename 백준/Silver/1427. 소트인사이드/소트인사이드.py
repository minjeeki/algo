N_lst = list(map(int, list(input())))
N_lst.sort(reverse=True)
print(*N_lst, sep='')