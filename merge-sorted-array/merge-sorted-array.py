class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        for i in range(n):
            nums1[i+m]=(nums2[i])
        nums1.sort()
        '''
        while m >0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m=m-1
            else:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
        while  n>0:
            nums1[m+n-1]=nums2[n-1]
            n=n-1
        while m >0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m=m-1
            else:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
        while  n>0:
            nums1[m+n-1]=nums2[n-1]
​
​
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
