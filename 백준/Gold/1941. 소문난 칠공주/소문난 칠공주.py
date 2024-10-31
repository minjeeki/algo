from collections import deque

board = [list(input()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def select_students(selected, dasom_count, x, y):
    global result

    if len(selected) == 7:
        if dasom_count >= 4 and is_connected(selected):
            result += 1
        return

    for i in range(x, 5):
        for j in range(y if i == x else 0, 5):
            if (i, j) not in selected:
                selected.add((i, j))
                select_students(selected, dasom_count + (1 if board[i][j] == 'S' else 0), i, j)
                selected.remove((i, j))

def is_connected(selected):
    queue = deque([next(iter(selected))])
    visited = set([next(iter(selected))])
    count = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (nx, ny) in selected and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                count += 1
    return count == 7

for i in range(5):
    for j in range(5):
        select_students(set([(i, j)]), 1 if board[i][j] == 'S' else 0, i, j)

print(result)
