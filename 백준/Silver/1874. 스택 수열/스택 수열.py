n = int(input())
# 만들고 싶은 수열 넣기
targets = [0] * n
for i in range(n):
    targets[i] = int(input())
num_lst = list(range(1, n+1))
t_idx = 0
stack = []
commands = []
can_make = True
for num_idx in range(n):
    if num_lst[num_idx] <= targets[t_idx]:
        stack.append(num_lst[num_idx])
        commands.append('+')
        # print(stack, stack[-1])
    while len(stack) != 0 and targets[t_idx] == stack[-1]:
        stack.pop()
        commands.append('-')
        t_idx += 1
    if len(stack) != 0 and stack[-1] > targets[t_idx]:
        can_make = False
        break
if can_make:
    print(*commands, sep='\n')
else:
    print('NO')

