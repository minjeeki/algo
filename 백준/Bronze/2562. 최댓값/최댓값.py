num = 9
max_num = 0
max_idx = -1
for idx in range(1, num + 1):
    now = int(input())
    if now > max_num:
        max_num = now
        max_idx = idx
print(max_num, max_idx, sep='\n')