# 실버 4. 덱
# pr-agent 테스트용 문제 풀이 코드 업로드 (스택 두개로 덱 구현)
import sys
input = sys.stdin.readline

front_stack = []
back_stack = []

N = int(input())
for _ in range(N):
    line = input().split()
    if line[0] == "push_front":
        front_stack.append(int(line[1]))
    elif line[0] == "push_back":
        back_stack.append(int(line[1]))
    elif line[0] == "pop_front":
        if not front_stack and not back_stack:
            print(-1)
        elif front_stack:
            print(front_stack.pop())
        else:
            # back_stack의 모든 요소를 front_stack으로 이동
            while back_stack:
                front_stack.append(back_stack.pop())
            print(front_stack.pop())
    elif line[0] == "pop_back":
        if not front_stack and not back_stack:
            print(-1)
        elif back_stack:
            print(back_stack.pop())
        else:
            # front_stack의 모든 요소를 back_stack으로 이동
            while front_stack:
                back_stack.append(front_stack.pop())
            print(back_stack.pop())
    elif line[0] == "size":
        print(len(front_stack) + len(back_stack))
    elif line[0] == "empty":
        print(1 if not front_stack and not back_stack else 0)
    elif line[0] == "front":
        if not front_stack and not back_stack:
            print(-1)
        elif front_stack:
            print(front_stack[-1])
        else:
            # back_stack의 모든 요소를 front_stack으로 이동
            while back_stack:
                front_stack.append(back_stack.pop())
            print(front_stack[-1])
    elif line[0] == "back":
        if not front_stack and not back_stack:
            print(-1)
        elif back_stack:
            print(back_stack[-1])
        else:
            # front_stack의 모든 요소를 back_stack으로 이동
            while front_stack:
                back_stack.append(front_stack.pop())
            print(back_stack[-1])
