class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        for i in range(1,len(height)):
            n=min(max(height[:i+1]),max(height[i:]))-height[i]
            ans+=n
        return ans
