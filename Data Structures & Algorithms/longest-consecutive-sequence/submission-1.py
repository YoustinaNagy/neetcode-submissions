class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums[:] = sorted( set(nums))
        # [2, 3, 4, 5, 10, 20]
        # print(nums)
        if len(nums)==0: return 0
        maxx=1;
        window =0
        l=0
        for r in range(1,len(nums)):
            if nums[r] - nums[l]==r-l:
                maxx= max(maxx,r-l+1) 
            else:
                l=r

        return maxx
        