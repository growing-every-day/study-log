# Runtime
# 596 ms
# Memory
# 24.1 MB
class Solution:
    def maxArea(self, height):
        
        # left, right 두개의 포인터를 가지고 양쪽에서 이동
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            # container는 짧은 height 를 기준으로 물이 담아지기 때문에, 짧은 포인터를 옮겨야 그 다음 container의 크기가 커질 가능성이 있다.
            if height[left]>=height[right]: # The right is shorter than left
                right-=1
            else: # The left is shorter than right
                left+=1
            
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))