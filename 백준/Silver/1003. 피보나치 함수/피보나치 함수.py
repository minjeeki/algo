def dfs(num):
    if dp[num][0] != -1:
        return dp[num]
    dp[num][0] = dfs(num - 1)[0] + dfs(num - 2)[0]
    dp[num][1] = dfs(num - 1)[1] + dfs(num - 2)[1]
    dp[num][2] = dfs(num - 1)[2] + dfs(num - 2)[2]
    return dp[num]

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[-1, -1, -1] for _ in range(N + 1)]
    dp[0] = [1, 0, 0]
    if N >= 1:
        dp[1] = [0, 1, 0]
    print(*dfs(N)[:2])