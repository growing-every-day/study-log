# https://www.acmicpc.net/problem/10773
import sys
read = sys.stdin.readline

K = int(read())
stack = []
for i in range(K):
	cmd = int(read())
	
	if cmd == 0:
		stack.pop()
	else:
		stack.append(cmd)
		
result=0
for i in stack:
	result+=i
print(result)
