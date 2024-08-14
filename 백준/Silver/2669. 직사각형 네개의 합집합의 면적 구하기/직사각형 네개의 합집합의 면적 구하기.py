paper = [[0 for row in range(100)] for col in range(100)]
cnt = 0
for square in range(4):
	x1, y1, x2, y2 = map(int, input().split())
	for row in range(x1, x2):
		for col in range(y1, y2):
			if paper[row][col] == 0:
				paper[row][col] = 1
				cnt += 1
print(cnt)