from itertools import combinations

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    k, *lstS = line
    for comb in combinations(lstS, 6):
        print(*comb)
    print()