N = int(input())
x_dict = {}
for _ in range(N):
    x, y = map(int, input().split())
    x_dict.setdefault(x, [])
    x_dict[x].append(y)
sorted_x_lst = sorted(list(x_dict.keys()))
for key in sorted_x_lst:
    x_dict[key].sort()
    for y in x_dict[key]:
        print(key, y)