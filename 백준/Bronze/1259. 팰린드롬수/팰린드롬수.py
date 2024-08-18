this_time = input()
while this_time != '0':
    if this_time == this_time[::-1]:
        print('yes')
    else:
        print('no')
    this_time = input()