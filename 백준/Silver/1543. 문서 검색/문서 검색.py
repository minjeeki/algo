doc = input()
len_doc = len(doc)
word = input()
len_wrd = len(word)
cnt = 0

idx = 0
while idx < len_doc:
    if doc[idx] == word[0]:
        for idx_word in range(1, len_wrd):
            if idx + idx_word < len_doc and doc[idx + idx_word] == word[idx_word]:
                continue
            else:
                idx += 1
                break
        else:
            idx += len_wrd
            cnt += 1
    else:
        idx += 1
print(cnt)
            