cur_num = 1
maken_set = set()
while cur_num <= 10000:
    if cur_num not in maken_set:
        print(cur_num)
    str_num = str(cur_num)
    next_num = cur_num
    for num in str_num:
        next_num += int(num)
    maken_set.add(next_num)
    cur_num += 1