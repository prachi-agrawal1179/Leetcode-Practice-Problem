class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=sum(nums)
        ans=[0]*n
        for i in reversed(range(n)):
    
            ans[i]=x
            x-=nums[i]
        return(ans)
