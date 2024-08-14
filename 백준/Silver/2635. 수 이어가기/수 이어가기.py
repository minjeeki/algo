num1 = int(input())
max_cnt = 0
max_arr = []
for num2 in range(1, num1 + 1):
    queue = []
    queue.append(num1)
    if num2 >= 0:
        queue.append(num2)
        while queue[-2] - queue[-1] >= 0:
            queue.append(queue[-2] - queue[-1])
            # print(queue)
    len_queue = len(queue)
    if max_cnt < len_queue:
        max_cnt = len_queue
        max_arr = queue
	# print(queue)
print(max_cnt)
print(*max_arr)