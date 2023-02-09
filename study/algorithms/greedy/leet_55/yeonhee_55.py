#Runtime 386 ms
# Memory 14.4 MB

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cmp_idx = 0
        for i, jump_count in enumerate(nums):
            if i > cmp_idx:
                return False
            cmp_idx = max(i+jump_count, cmp_idx)

            if cmp_idx >= len(nums)-1:
                return True


# 아래는 시간초과 코드
# class Solution(object):

#     def dfs(self, i, nums, nums_tuple):
#         if i == len(nums)-1:
#             return
            
#         jump_count = nums_tuple[i][1]
#         jump_enable_idxes = nums_tuple[i+1 : i+1+jump_count]
#         if 0 == len(jump_enable_idxes):
#             return

#         jump_enable_idxes = sorted(jump_enable_idxes,  key = lambda x : (-x[1], -x[0]) )

#         max_tuple = jump_enable_idxes[0]
#         # 현재 인덱스 + 현재 인덱스에서 점프 가능 횟수 >= 마지막 인덱스 
#         org_cur_idx = max_tuple[0]
#         if org_cur_idx + max_tuple[1] >= len(nums)-1:
#             self.result = True
#             return

#         for tup in jump_enable_idxes:
#             self.dfs(tup[0],nums,nums_tuple)

#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) == 1:
#             return True
#         nums_tuple = []
#         for i, n in enumerate(nums):
#             nums_tuple.append((i,n))
#         self.result = False
#         self.dfs(0, nums, nums_tuple)
#         return self.result

s = Solution()
print(s.canJump([0])) # true
print(s.canJump([4,2,0,0,1,1,4,4,4,0,4,0]))# true
print(s.canJump([4,0,4,2,2,0,1,3,3,0,3]))#true
print(s.canJump([3,0,8,2,0,0,1]))#true
print(s.canJump([2,3,1,1,4]))#true
print(s.canJump([3,2,1,0,4]))#false
print(s.canJump([1,2,3]))#true
print(s.canJump([1,2]))#true
print(s.canJump([0,2,3]))#false