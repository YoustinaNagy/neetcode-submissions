class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tnum = 0
        snum = 0
        while snum < len(s) and tnum < len(t):
            if s[snum] == t[tnum]:
                snum += 1
                tnum += 1
            else:
                tnum += 1

        return snum == len(s)


                    
        