# https://www.acmicpc.net/problem/10828
# 헤헷 주석이 //이 아니라 #이라니.,,,,,,
import sys
read = sys.stdin.readline

N = int(read())

stack = []

for i in range(N):
    cmd = read().split()

    if cmd[0] == "push":
        stack.insert(len(stack), cmd[1]) #stack.append(command[1])써도 됨
    elif cmd[0] == "pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
