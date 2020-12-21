class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[1]*n
        r=[1]*n
        ans=[1]*n
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        
        for j in reversed(range(n-1)):
            r[j]=r[j+1]*nums[j+1]
        
        for k in range(n):
            ans[k]=l[k]*r[k]
        return ans
            
