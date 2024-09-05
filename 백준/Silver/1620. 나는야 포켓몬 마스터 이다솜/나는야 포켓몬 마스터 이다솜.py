N, M = map(int, input().split())
monster_by_idx = [None] * (N + 1)
monster_by_name = {}
for num in range(1, N+1):
    monster_name = input()
    monster_by_idx[num] = monster_name
    monster_by_name[monster_name] = num
for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        print(monster_by_idx[int(quiz)])
    else:
        print(monster_by_name[quiz])