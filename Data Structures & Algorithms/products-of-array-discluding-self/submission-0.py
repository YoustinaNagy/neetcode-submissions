class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]

        # [1, 2, 6, 24]
        # [24, 24, 12, 4]

        # [24,12,8,6]
        pre =[]
        post= [0] * len(nums)
        out = [0] * len(nums)
        add = 1
        for num in nums:
            add = add * num
            # print(add)
            pre.append(add)

        add=1
        for i in range(len(nums)-1 , -1 ,-1):
            add = add * nums[i]
            post[i]=add

        for i in range(len(nums)):
            val = 1
            if i > 0:
                val *= pre[i-1]
            if i < len(nums) - 1:
                val *= post[i+1]
            out[i] = val
        # print(pre)
        # print(post)
        # print(out)
        return out


        