next_n = 0
print_lst = ['FizzBuzz', 'Fizz', 'Buzz']
for idx in range(3):
    now_print = input()
    if now_print not in print_lst:
        next_n = int(now_print) + (3 - idx)
        break
if next_n % 3 == 0 and next_n % 5 == 0:
    print(print_lst[0])
elif next_n % 3 == 0:
    print(print_lst[1])
elif next_n % 5 == 0:
    print(print_lst[2])
else:
    print(next_n)