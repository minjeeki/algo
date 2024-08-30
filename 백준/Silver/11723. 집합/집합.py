import sys
# # 배열로 풀면 시간 초과 발생
M = int(sys.stdin.readline())
S = [0] * 21
result = []
for _ in range(M):
    commands = sys.stdin.readline().split()
    if len(commands) == 2:
        num = int(commands[1])
    command = commands[0]
    if command == 'add':
        S[num] = 1
    elif command == 'remove':
        S[num] = 0
    elif command == 'check':
        print(S[num])
    elif command == 'toggle':
        S[num] = 1 if S[num] == 0 else 0
    elif command == 'all':
        S = [1] * 21
    else:
        S = [0] * 21
print(*result, sep="\n")