import sys

class Stack:
    def __init__(self, N):
        self.top = -1
        self.stack = [0] * N

    def s_push(self, item):
        self.top += 1
        self.stack[self.top] = item
    
    def s_pop(self):
        if self.top == -1:
            return -1
        else:
            num = self.stack[self.top]
            self.top -= 1
            return num
    
    def s_size(self):
        return self.top + 1
    
    def s_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0
    
    def s_top(self):
        if self.top == -1:
            return -1
        else:
            return self.stack[self.top]

N = int(sys.stdin.readline())
stack = Stack(N)
for _ in range(N):
    command_lst = sys.stdin.readline().split()
    command = command_lst[0]
    if command == 'push':
        stack.s_push(int(command_lst[1]))
    elif command == 'pop':
        print(stack.s_pop())
    elif command == 'size':
        print(stack.s_size())
    elif command == 'empty':
        print(stack.s_empty())
    elif command == 'top':
        print(stack.s_top())