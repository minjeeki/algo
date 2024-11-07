def move_next(range_start, range_end, cur_idx):
    for next_num in range(range_start, range_end):
        if not visited[next_num]:
            visited[next_num] = True
            num_lst.append(next_num)
            dfs(next_num, cur_idx + 1)
            visited[next_num] = False
            num_lst.pop()

def dfs(cur_num, cur_idx):
    if cur_idx == k:
        answers.append(''.join(list(map(str, num_lst))))
        return
    
    if signs[cur_idx] == '<':
        move_next(cur_num + 1, 10, cur_idx)
    elif signs[cur_idx] == '>':
        move_next(0, cur_num, cur_idx)


k = int(input())
signs = input().split()

visited = [False] * 10
answers = []
num_lst = []

for i in range(10):
    visited[i] = True
    num_lst.append(i)
    dfs(i, 0)
    num_lst.pop()
    visited[i] = False
print(answers[-1], answers[0], sep='\n')