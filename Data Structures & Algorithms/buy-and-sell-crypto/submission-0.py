class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minn = prices[0]
        for price in prices:
            res = max(res,  price - minn)
            if price< minn:
                minn=price
        return res
        
        