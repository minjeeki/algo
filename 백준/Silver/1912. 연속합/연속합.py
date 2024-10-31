n = int(input())
numlst = list(map(int, input().split()))

dp = [0] * n
dp[0] = numlst[0]
max_sum = dp[0]

# 연속합 갱신
for i in range(1, n):
    dp[i] = max(numlst[i], dp[i - 1] + numlst[i])
    max_sum = max(max_sum, dp[i])

print(max_sum)
