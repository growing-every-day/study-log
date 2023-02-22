from typing import List
from bisect import bisect_left
import sys

def lengthOfLIS(nums: List[int]) -> int:
    stack = []
    tmp = []

    for num in nums:
        if not stack or stack[-1] < num:
            stack.append(num)
            tmp.append((len(stack)-1, num))
        else:
            stack[bisect_left(stack, num)] = num
            tmp.append((bisect_left(stack, num), num))

    ans = []
    last_idx = len(stack)-1
    
    for i in range(len(tmp)-1, -1, -1):
        if tmp[i][0] == last_idx:
            ans.append(tmp[i][1])
            last_idx -= 1

    return len(stack), ans


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    length, sub = lengthOfLIS(nums)
    print(length)
    print(*sub[::-1])