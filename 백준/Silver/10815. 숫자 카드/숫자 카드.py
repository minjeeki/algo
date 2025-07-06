N = int(input())
cards = set(map(int, input().split()))
M = int(input())
tests = list(map(int, input().split()))

tests = [1 if num in cards else 0 for num in tests]

print(*tests)