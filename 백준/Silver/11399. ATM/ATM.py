N = int(input())
time_lst = sorted(list(map(int, input().split())))
result_lst = [time_lst[0]] + ([0] * (N - 1))
result = time_lst[0]
for idx in range(1, N):
    result_lst[idx] = result_lst[idx - 1] + time_lst[idx]
    result += result_lst[idx]
print(result)