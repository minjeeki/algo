X = input()
convert_cnt = 0
while int(X) >= 10:
    num = 0
    for n in X:
        num += int(n)
    X = str(num)
    convert_cnt += 1
if int(X) % 3 == 0:
    print(convert_cnt, 'YES', sep='\n')
else:
    print(convert_cnt, 'NO', sep='\n')