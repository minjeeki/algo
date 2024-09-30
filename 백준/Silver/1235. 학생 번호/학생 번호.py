N = int(input())

students = [input() for _ in range(N)]
for k in range(1, len(students[0]) + 1):
    # print(*[students[i][(-1 * k):] for i in range(N)])
    num_set = set([students[i][(-1 * k):] for i in range(N)])
    # print(list(num_set))
    if len(num_set) == N:
        print(k)
        break