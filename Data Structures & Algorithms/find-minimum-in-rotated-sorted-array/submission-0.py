class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        r=len(nums)-1
        res = float('inf')
        while(l<=r):
            m = (l + r) // 2
            res=min (nums[m], res)
            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m-1
            res=min(nums[m], res)
        return res 


        