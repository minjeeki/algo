import sys
sys.setrecursionlimit(10 ** 6)

def ft_dfs(cur_idx, before_status):
    if cur_idx == (N - 1):
        return 1
    
    if dp[cur_idx][before_status] != -1:
        return dp[cur_idx][before_status]

    res = 0
    if before_status == -1:
        res += ft_dfs(cur_idx + 1, -1)
        res += ft_dfs(cur_idx + 1, 0)
        res += ft_dfs(cur_idx + 1, 1)
    elif before_status == 0:
        res += ft_dfs(cur_idx + 1, -1)
        res += ft_dfs(cur_idx + 1, 1)
    elif before_status == 1:
        res += ft_dfs(cur_idx + 1, -1)
        res += ft_dfs(cur_idx + 1, 0)
    
    dp[cur_idx][before_status] = res % 9901
    return dp[cur_idx][before_status]

N = int(input())
dp = [[-1 for _ in range(3)] for _ in range(N)]
print(ft_dfs(-1, -1))