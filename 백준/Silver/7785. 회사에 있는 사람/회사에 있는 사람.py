N = int(input())
enter_set = set()
for _ in range(N):
    name, status = input().split()
    if status == 'enter':
        enter_set.add(name)
    elif status == 'leave':
        enter_set.remove(name)
total_lst = sorted(list(enter_set), reverse=True)
print(*total_lst, sep='\n')