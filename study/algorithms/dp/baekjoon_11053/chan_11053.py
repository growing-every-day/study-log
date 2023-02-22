from typing import List
from bisect import bisect_left
import sys

def lengthOfLIS(nums: List[int]) -> int:
    stack = []

    for num in nums:
        if not stack or stack[-1] < num:
            stack.append(num)
        else:
            stack[bisect_left(stack, num)] = num

    return len(stack)

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    length = lengthOfLIS(nums)
    print(length)