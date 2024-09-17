A, B = map(int, input().split())
modi_B = B
cnt = 0
while modi_B > A:
    if modi_B % 10 == 1:
        modi_B = modi_B // 10
        cnt += 1
    elif modi_B % 2 == 0:
        while modi_B % 2 == 0 and modi_B > A:
            modi_B = modi_B // 2
            cnt += 1
    else:
        cnt = -1
        break
print(cnt + 1 if modi_B == A else -1)