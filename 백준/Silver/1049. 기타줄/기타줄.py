N, M = map(int, input().split())    # 끊어진 기타줄 수 & 기타줄 브랜드 수
min_price = [100 * 1000, 100 * 1000]
for _ in range(M):
    by_package, by_one = map(int, input().split())
    min_price[0] = min(min_price[0], by_package)
    min_price[1] = min(min_price[1], by_one)

cnt_only_one = N * min_price[1]
cnt_only_package = (N // 6 if N % 6 == 0 else N // 6 + 1) * min_price[0]
cnt_collabo = (N // 6) * min_price[0] + (N % 6) * min_price[1]

min_cost = min(cnt_only_one, cnt_only_package, cnt_collabo)
print(min_cost)