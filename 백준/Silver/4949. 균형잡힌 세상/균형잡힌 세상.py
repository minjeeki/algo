sentence = input()
while sentence != '.':
    stack = []
    is_balance = 'yes'
    for char in sentence:
        if char in ['(', '[']:
            stack.append(char)
        elif char == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif char == ')' and (len(stack) == 0 or stack[-1] != '('):
            is_balance = 'no'
            break
        elif char == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        elif char == ']' and (len(stack) == 0 or stack[-1] != '['):
            is_balance = 'no'
            break
    if len(stack) != 0:
        is_balance = 'no'
    print(is_balance)
    sentence = input()