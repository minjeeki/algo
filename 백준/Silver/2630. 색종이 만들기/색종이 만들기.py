def ft_check_square(sx, sy, size):
    global total_cnt_white, total_cnt_blue

    cnt_white = 0
    cnt_blue = 0
    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if grid[i][j] == 0:
                cnt_white += 1
            else:
                cnt_blue += 1
        if cnt_white != 0 and cnt_blue != 0:
            for nx in range(sx, sx + size, size // 2):
                for ny in range(sy, sy + size, size // 2):
                    ft_check_square(nx, ny, size // 2)
            return
    if cnt_white == size * size:
        total_cnt_white += 1
    elif cnt_blue == size * size:
        total_cnt_blue += 1


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

total_cnt_white = 0
total_cnt_blue = 0

ft_check_square(0, 0, N)
print(total_cnt_white, total_cnt_blue, sep='\n')