class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            curr,l,r=i,i+1,len(nums)-1
            while l<r:
                _sum = nums[curr] + nums[l] + nums[r]
​
                if _sum==0:
                    ans.add((nums[curr],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif _sum<0:
                    l+=1
                else:
                    r-=1
        
        return ans
                    
        
            
        
