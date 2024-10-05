N, M, B = map(int, input().split())
hi_dict = {}
min_time = 256 * N * M
height = 0

min_hi = 256
max_hi = 0
sum_place = 0
for _ in range(N):
    for hi in list(map(int, input().split())):
        hi_dict.setdefault(hi, 0)
        hi_dict[hi] += 1
        if min_hi > hi:
            min_hi = hi
        if max_hi < hi:
            max_hi = hi
        sum_place += hi

for tar_h in range(min_hi, max_hi + 1):
    if (tar_h * N * M) > (B + sum_place):
        continue
    time = 0
    for cur_h in hi_dict.keys():
        if cur_h == tar_h:
            continue
        elif cur_h > tar_h:
            time += (cur_h - tar_h) * hi_dict[cur_h] * 2
        elif cur_h < tar_h:
            time += (tar_h - cur_h) * hi_dict[cur_h]
    if time < min_time:
        min_time = time
        height = tar_h
    if time == min_time:
        height = max(height, tar_h)
print(min_time, height)