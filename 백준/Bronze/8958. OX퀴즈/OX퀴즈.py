T = int(input())
for _ in range(T):
    quiz_str = input()
    combo = 0
    total = 0
    for quiz in quiz_str:
        if quiz == 'O':
            combo += 1
            total += combo
        else:
            combo = 0
    print(total)