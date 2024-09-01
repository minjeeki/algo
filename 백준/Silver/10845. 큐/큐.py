N = int(input())
q = [0] * N
front = 0
rear = 0
for _ in range(N):
    commands = input().split()
    if commands[0] == 'push':
        q[rear] = commands[1]
        rear += 1
    elif commands[0] == 'empty':
        print(1 if front == rear else 0)
    elif commands[0] == 'size':
        print(rear - front)
    elif front == rear:
        print(-1)
    elif commands[0] == 'pop':
        print(q[front])
        front += 1
    elif commands[0] == 'front':
        print(q[front])
    elif commands[0] == 'back':
        print(q[rear - 1])