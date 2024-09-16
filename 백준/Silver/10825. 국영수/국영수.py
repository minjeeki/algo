N = int(input())
students = [0 for _ in range(N)]
for idx in range(N):
    students[idx] = input().split()
    for i in range(1, 4):
        students[idx][i] = int(students[idx][i])
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for pi in range(N):
    print(students[pi][0])