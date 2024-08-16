C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seats = [[0] * R for _ in range(C)]
    idx_direction = 0
    start_x = 0
    start_y = 0
    for num in range(1, C * R + 1):
        seats[start_y][start_x] = num
        if num == K:
            print(start_y + 1, start_x + 1)
            break
        next_x = start_x + directions[idx_direction][1]
        next_y = start_y + directions[idx_direction][0]
        if 0 <= next_x < R and 0 <= next_y < C and seats[next_y][next_x] == 0:
            pass
        else:
            # print('direction change')
            idx_direction = (idx_direction + 1) % 4
        start_x += directions[idx_direction][1]
        start_y += directions[idx_direction][0]
        # print(num)
    # print(*seats, sep='\n')