N, K = map(int, input().split())
coins = [0] * N
for idx in range(N):
    coins[idx] = int(input())
cnt = 0
for i in range(N-1,-1,-1):
    now_cnt = K // coins[i]
    if now_cnt > 0:
        K = K % coins[i]
        cnt += now_cnt
        if K == 0:
            break
print(cnt)