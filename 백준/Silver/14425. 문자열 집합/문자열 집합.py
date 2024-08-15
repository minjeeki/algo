n, m = map(int, input().split())
set_s = set()
for _ in range(n):
    set_s.add(input())
cnt = 0
for _ in range(m):
    str_need_test = input()
    if str_need_test in set_s:
        cnt += 1
print(cnt)