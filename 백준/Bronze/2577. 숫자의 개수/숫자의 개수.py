multiple_num = 1
for _ in range(3):
    multiple_num *= int(input())
num_str = str(multiple_num)
for char in range(10):
    print(num_str.count(str(char)))