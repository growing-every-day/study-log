## https://www.acmicpc.net/problem/2512

## 인풋 받아옴
N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

## 바이너리 서치 
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2 ## 상한액
        total = 0
        for budget in budgets:
            total += min(budget, mid)
        if total > M:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(binary_search(0, max(budgets)))