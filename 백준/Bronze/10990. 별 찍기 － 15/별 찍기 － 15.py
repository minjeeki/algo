N = int(input())

blank = N - 1
print(f"{' ' * (blank)}{'*'}")
blank -= 1
middle = 1
is_not_end = 1
while blank >= 0:
    if blank == 0:
        is_not_end = 0
    print(f"{' ' * (blank)}*{' ' * (middle)}*{' ' * (is_not_end)}")
    middle += 2
    blank -= 1