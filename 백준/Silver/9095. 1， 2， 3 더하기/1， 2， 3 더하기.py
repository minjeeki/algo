def ft_dfs(left_num):
    if left_num == 0:
        return 1
    if left_num < 0:
        return 0

    if dp[left_num] != -1:
        return dp[left_num]

    if left_num == 1:
        dp[left_num] = ft_dfs(left_num - 1)
    elif left_num == 2:
        dp[left_num] = ft_dfs(left_num - 1) + ft_dfs(left_num - 2)
    else:
        dp[left_num] = ft_dfs(left_num - 1) + ft_dfs(left_num - 2) + ft_dfs(left_num - 3)

    return dp[left_num]

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [-1] * (N + 1)
    print(ft_dfs(N))