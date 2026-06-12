class Solution:
    def search(self, nums: List[int], target: int) -> int:


        #   l   m   r
        # // 1 2 3 4 5
        # //     4
        #        2
        r =len(nums)-1
        l=0
        while l<=r :
            mid = int(r+l/2)
            if nums[mid]>target:
                r= mid-1
            elif nums[mid]<target:
                l= mid+1
            else : return mid
        
        return -1

        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return -1
        