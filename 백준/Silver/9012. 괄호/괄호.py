T = int(input())
for tc in range(1, T+1):
    stack = []
    input_lst = input()
    result = ''
    for c in input_lst:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 'NO'
                break
    if result != 'NO':
        if len(stack) != 0:
            result = 'NO'
        else:
            result = 'YES'
    print(result)