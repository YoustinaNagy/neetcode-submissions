class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
        