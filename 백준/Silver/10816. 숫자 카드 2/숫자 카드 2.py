N = int(input())
n_lst = list(map(int, input().split()))
dict_n = {}
for n in n_lst:
    dict_n.setdefault(n, 0)
    dict_n[n] += 1
M = int(input())
m_lst = list(map(int, input().split()))
for m in m_lst:
    if m in dict_n.keys():
        print(dict_n[m], end=' ')
    else:
        print(0, end=' ')