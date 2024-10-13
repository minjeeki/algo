from collections import deque

# 지역 개수, 예은이 수색 범위, 길의 개수
n, m, r = map(int, input().split())
node_lst = [[] for _ in range(n + 1)]
node_lst[0] = None
# 각 구역에 있는 아이템 수
items = [0] + list(map(int, input().split()))
for i in range(r):
    # 길 양 끝에 존재하는 지역 번호 a,b 그리고 길의 길이
    a, b, l = map(int, input().split())
    node_lst[a].append((b, l))
    node_lst[b].append((a, l))

max_get_item = 0
for user_point in range(1, n + 1):
    added = set()
    added.add(user_point)
    deq = deque()
    deq.append([user_point, m])
    cur_get_item = items[user_point]
    while deq:
        target = deq.popleft()
        for t_nod in node_lst[target[0]]:
            if t_nod[1] <= target[1]:
                deq.append([t_nod[0], target[1] - t_nod[1]])
                if t_nod[0] not in added:
                    cur_get_item += items[t_nod[0]]
                    added.add(t_nod[0])
    # print('---', user_point, cur_get_item)
    max_get_item = max(max_get_item, cur_get_item)
print(max_get_item)