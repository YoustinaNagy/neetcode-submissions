class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums[:]=sorted(nums)
        seen=set()
        counted=set()
        for i in range(len(nums)):
            if i in counted:
                continue
            counted.add(i)
            l = i+1
            r= len(nums)-1
            while(l<r):
                total= nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    seen.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
        return list(seen)
        