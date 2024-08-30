N, M = map(int, input().split())
names = set()
job = set()
for _ in range(N):
    names.add(input())
for _ in range(M):
    name = input()
    if name in names:
        job.add(name)
print(len(job), *sorted(list(job)), sep="\n")