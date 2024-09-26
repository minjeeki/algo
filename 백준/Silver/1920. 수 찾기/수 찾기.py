N = int(input())
n_lst = set(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))
for num in m_lst:
    if num in n_lst:
        print(1)
    else:
        print(0)