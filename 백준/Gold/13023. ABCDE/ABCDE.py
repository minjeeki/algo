from collections import deque

def dfs(cur_friend, connection):
    global is_in_line

    if connection == 5:
        is_in_line = 1
        return
    elif connection > 5:
        return

    if is_in_line == 0:
        deq = deque(near_lst[cur_friend])
        while deq:
            next_candi = deq.popleft()
            if next_candi not in visited:
                visited.add(next_candi)
                dfs(next_candi, connection + 1)
                visited.remove(next_candi)

N, M = map(int, input().split())
near_lst = [[] for _ in range(N)]
for i in range(M):
    f1, f2 = map(int, input().split())
    near_lst[f1].append(f2)
    near_lst[f2].append(f1)

is_in_line = 0
for start_f in range(N):
    visited = set([start_f])
    dfs(start_f, 1)

print(is_in_line)