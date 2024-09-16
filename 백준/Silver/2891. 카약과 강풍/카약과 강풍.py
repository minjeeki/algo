# N : 팀수 / S : 카약 손상 팀 수 / R : 하나 더 가져온 팀 수
N, S, R = map(int, input().split())
set_d = set(map(int, input().split()))
has_spare = list(map(int, input().split()))
for idx in range(R):
    if has_spare[idx] in set_d:
        set_d.remove(has_spare[idx])
        has_spare[idx] = -1
has_spare.sort()
for idx in range(R):
    if has_spare[idx] > 0 and has_spare[idx] - 1 in set_d:
        set_d.remove(has_spare[idx] - 1)
    elif has_spare[idx] > 0 and has_spare[idx] + 1 in set_d:
        set_d.remove(has_spare[idx] + 1)
print(len(set_d))