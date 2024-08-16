N, K = map(int, input().split())
tem_lst = list(map(int, input().split()))
if K == 1:
    print(max(tem_lst))
else:
    combo_lst = [0] * (N - K + 1)
    combo_lst[0] = sum(tem_lst[:K])
    for i in range(1, N - K + 1):
        combo_lst[i] = combo_lst[i - 1] - tem_lst[i - 1] + tem_lst[i + K - 1]
    print(max(combo_lst))
    # print(combo_lst)