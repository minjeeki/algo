N, K = map(int, input().split())
students = [[0] * 7 for _ in range(2)] # 0학년은 비워둘 심산
for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1
min_room = 0
for s in range(2):
    for y in range(1, 7):
        min_room += students[s][y] // K
        if students[s][y] % K != 0:
            min_room += 1
print(min_room)