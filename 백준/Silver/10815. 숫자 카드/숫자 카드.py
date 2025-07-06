N = int(input())
cards = set(map(int, input().split()))
M = int(input())
tests = list(map(int, input().split()))

for idx in range(M):
    tests[idx] = 1 if tests[idx] in cards else 0

print(*tests)