dwarfs = [0] * 9

for i in range(9):
    dwarfs[i] = int(input())
sum_height = sum(dwarfs)
found_impo = False

for del_idx1 in range(8):
    for del_idx2 in range(del_idx1 + 1, 9):
        if sum_height - (dwarfs[del_idx1] + dwarfs[del_idx2]) == 100:
            found_impo = True
            dwarfs[del_idx1] = 0
            dwarfs[del_idx2] = 0
            break
    if found_impo == True:
        print(*sorted(dwarfs)[2:], sep='\n')
        break