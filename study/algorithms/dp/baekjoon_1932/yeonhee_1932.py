import sys
input = sys.stdin.readline

# 	37732kb	144ms
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split(" "))))

dp = [[ 0 for i in range(n)] for j in range(n)]

for r in range(n-1, 0, -1):
    for c in range(len(arr[r])-1):
        arr[r-1][c] += max(arr[r][c],arr[r][c+1])

print(arr[0][0])