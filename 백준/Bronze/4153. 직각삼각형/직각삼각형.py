def check_end(lines):
    for line in lines:
        if line != 0:
            return(False)
    return(True)

lines = sorted(list(map(int, input().split())))
is_end = check_end(lines)
while is_end == False:
    if (lines[2] ** 2) == (lines[0] ** 2) + (lines[1] ** 2):
        print("right")
    else:
        print("wrong")
    lines = sorted(list(map(int, input().split())))
    is_end = check_end(lines)