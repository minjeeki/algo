N = int(input())

lie_row = 0
lie_col = 0

matrix = [[] for _ in range(N)]
for idx1 in range(N):
    line1 = input()
    space1 = line1.split('X')
    for i in range(len(space1)):
        if len(space1[i]) >= 2:
            lie_row += 1
    matrix[idx1] = list(line1)
zip_matrix = list(zip(*matrix))
for idx2 in range(N):
    line2 = ''.join(zip_matrix[idx2])
    space2 = line2.split('X')
    for j in range(len(space2)):
        if len(space2[j]) >= 2:
            lie_col += 1
print(lie_row, lie_col)