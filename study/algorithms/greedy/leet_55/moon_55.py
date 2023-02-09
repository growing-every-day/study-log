class Solution(object):
    def canJump(self, nums):
        jump = 0

        for i in range(len(nums)-1):
            jump = max(jump, nums[i])

            if jump==0 :
                return False

            jump -= 1
        
        return True
 # Runtime : 376 ms, Memory : 14.5 MB     
