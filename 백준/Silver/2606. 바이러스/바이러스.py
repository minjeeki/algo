def ft_dfs(start_idx):
    visited[start_idx] = True
    for item in near_lst[start_idx]:
        if visited[item] == False:
            global total_cnt
            total_cnt += 1
            ft_dfs(item)
        

N = int(input())
near_lst = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
connections = int(input())
for _ in range(connections):
    com1, com2 = map(int, input().split())
    near_lst[com1].append(com2)
    near_lst[com2].append(com1)
total_cnt = 0
ft_dfs(1)
print(total_cnt)