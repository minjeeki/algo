name = input()
len_alphabet = ord('Z') - ord('A') + 1
alphabet_cnt = [0] * (len_alphabet)
for char in name:
    alphabet_cnt[ord(char) - ord('A')] += 1
# print(alphabet_cnt)
before_word = []
after_word = []
odd_num_idx = -1
for idx in range(len_alphabet):
    # alphabet이 없음
    if alphabet_cnt[idx] == 0:
        continue
    # alphabet 개수가 홀수임
    if alphabet_cnt[idx] % 2 == 1:
        if odd_num_idx == -1:
            odd_num_idx = idx
            alphabets = chr(idx + ord('A')) * (alphabet_cnt[idx] // 2)
            before_word.append(alphabets)
            after_word.append(alphabets)
        else:
            odd_num_idx = -100
            break
    # alphabet이 짝수임
    else:
        alphabets = chr(idx + ord('A')) * (alphabet_cnt[idx] // 2)
        before_word.append(alphabets)
        after_word.append(alphabets)
if odd_num_idx == -100:
    new_word = "I'm Sorry Hansoo"
else:
    before_word = ''.join(before_word)
    after_word = ''.join(after_word[::-1])
    if odd_num_idx >= 0:
        center_chr = chr(odd_num_idx + ord('A'))
    else:
        center_chr = ''
    new_word = before_word + center_chr + after_word
print(new_word)