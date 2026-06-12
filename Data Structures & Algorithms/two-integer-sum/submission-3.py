class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = list(enumerate(nums))
        sort=sorted(indexed , key=lambda x:x[1])
        
        n=len(nums)
        biggest= n-1
        smallest = 0
        while(biggest>smallest):
            big=sort[biggest][1]
            small=sort[smallest][1]
            if big+small>target:
                biggest-=1
            elif big+small<target:
                smallest+=1
            else:
                s=sort[smallest][0]
                b=sort[biggest][0]
                return [min(b,s),max(b,s)]
        
        return []
        