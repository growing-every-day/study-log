import sys
input = sys.stdin.readline

# 	32276kb, 52ms
def binary_search():
    right = max(budget)
    left = 1

    res = []
    while left <= right:
        mid = (left+right) // 2

        cal_budget = 0
        for b in budget:
            cal_budget += min(b, mid)

        if cal_budget > total:
            right = mid-1
        else:
            res.append(mid)
            left = mid+1

    return max(res)



if "__main__" == __name__:
    n = int(input())
    budget = list(map(int, input().split(" ")))
    total = int(input())

    print(binary_search())
