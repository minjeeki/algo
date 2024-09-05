N = int(input())
spots = [[] for _ in range(N)]
for idx in range(N):
    spots[idx] = list(map(int, input().split()))
spots = sorted(spots, key=lambda x: (x[1], x[0]))
for spot in spots:
    print(*spot)