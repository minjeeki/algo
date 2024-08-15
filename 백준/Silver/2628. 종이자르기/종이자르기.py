p_wid, p_hei = map(int, input().split())
cut_cnt = int(input())
cut_lst = [[0] for _ in range(2)]
for _ in range(cut_cnt):
    dot_line, num = map(int, input().split())
    cut_lst[dot_line].append(num)
cut_lst[0] = sorted(cut_lst[0]) + [p_hei]
cut_lst[1] = sorted(cut_lst[1]) + [p_wid]
# print(cut_lst)
max_hei = 0
for h_idx in range(len(cut_lst[0]) - 1):
    mini_hei = cut_lst[0][h_idx + 1] - cut_lst[0][h_idx]
    if mini_hei > max_hei:
        max_hei = mini_hei
max_wid = 0
for w_idx in range(len(cut_lst[1]) - 1):
    mini_wid = cut_lst[1][w_idx + 1] - cut_lst[1][w_idx]
    if mini_wid > max_wid:
        max_wid = mini_wid
print(max_hei * max_wid)