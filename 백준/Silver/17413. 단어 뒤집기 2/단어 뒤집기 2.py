S = input()
len_s = len(S)
new_word = []
rev_word = []
idx = 0
while idx < len_s:
    if S[idx] == '<':
        if len(rev_word) != 0:
            new_word.append(''.join(rev_word[::-1]))
            rev_word = []
        while S[idx] != '>':
            new_word.append(S[idx])
            idx += 1
        new_word.append(S[idx])
        idx += 1
    elif S[idx] == ' ':
        new_word.append(''.join(rev_word[::-1]))
        rev_word = []
        new_word.append(' ')
        idx += 1
    else:
        rev_word.append(S[idx])
        idx += 1
if len(rev_word) != 0:
    new_word.append(''.join(rev_word[::-1]))
    rev_word = []
print(''.join(new_word))