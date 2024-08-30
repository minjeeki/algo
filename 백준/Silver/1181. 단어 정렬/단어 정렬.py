N = int(input())
len_dict = {}
for _ in range(N):
    word = input()
    len_word = len(word)
    len_dict.setdefault(len_word, set())
    len_dict[len_word].add(word)
dict_keys = sorted(len_dict.keys())
for key in dict_keys:
    print(*sorted(list(len_dict[key])), sep="\n")