import sys
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

# 35456kb	68ms
n = int(input())
arr = list(map(int, input().split(" ")))
lis = []
indexes = [0 for i in range(n)]
ans = 0

for i,num in enumerate(arr):
    if not lis:
        lis.append(num)
        ans += 1
        indexes[i] = 0
        continue
    
    if lis[-1] < num:
        lis.append(num)
        ans += 1
        indexes[i] = len(lis)-1
    else:
        index = bisect_left(lis, num)
        lis[index] = num
        indexes[i] = index
    
print(ans)
# print(*lis)
# print(*indexes)
res = []

tmp = ans-1
for i in range(len(indexes)-1, -1, -1):
    if indexes[i] == tmp:
        res.append(arr[i])
        tmp -= 1

res.reverse()
print(*res)
# 참고: 
# https://velog.io/@uoayop/BOJ-12015-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-Python
