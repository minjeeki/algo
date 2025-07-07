T = int(input())
MAX_L = 5000
MOD = 1000000007

dp = [0] * (MAX_L + 1)
dp[0] = 1

for i in range(2, MAX_L + 1, 2):
    for j in range(0, i, 2):
        dp[i] = (dp[i] + dp[j] * dp[i - 2 - j]) % MOD

for _ in range(T):
    L = int(input())
    print(dp[L])