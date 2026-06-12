class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        l=0
        if len(s)==0: return 0
        ch.add(s[l])
        r=1
        res=0
        while (r < len(s)) :
            res= max(res,len(ch))
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            r+=1
        return max(res,len(ch))
            
