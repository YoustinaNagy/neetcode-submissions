class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #      [1,2,3,4]
        # pre  [-,1,2,6]
        # post [24,12,4,-]
        # res. [24, 12,8,6]
        n=len(nums)
        pre = [1]*n
        post = [1]*n
        res=[0]*n
        
        count = 1
        for i in range (n-1):
            count = count* nums[i]
            pre[i+1]= count
            
        count = 1
        for i in range (n-1 ,0 ,-1):
            count = count* nums[i]
            post[i-1]= count

        for i in range(n):
            res[i]= post[i]*pre[i]
        
        return res
        