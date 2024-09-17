N = int(input())        # 로프 개수
rope = [int(input()) for _ in range(N)]
rope.sort()
max_weight = 0
for idx in range(N):
    max_weight = max(max_weight, rope[idx] * (N - idx))
print(max_weight)