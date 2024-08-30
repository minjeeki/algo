N = int(input())
factorial_n = 1
while N > 1:
    factorial_n *= N
    N -= 1
factorial_n = str(factorial_n)
len_factorial = len(factorial_n)
cnt = 0
for i in range(len_factorial - 1, -1, -1):
    if factorial_n[i] != '0':
        break
    cnt += 1
print(cnt)