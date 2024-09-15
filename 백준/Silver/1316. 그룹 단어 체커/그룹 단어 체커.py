N = int(input())
cnt_group_word = 0
for _ in range(N):
    word = input()
    before_char = ''
    set_char = set()
    for idx in range(len(word)):
        if word[idx] not in set_char:
            set_char.add(word[idx])
            before_char = word[idx]
        elif before_char != word[idx]:
            break
    else:
        cnt_group_word += 1
print(cnt_group_word)