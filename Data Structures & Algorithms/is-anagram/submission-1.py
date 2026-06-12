from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smap = Counter(s) 
        '''
        smap = Counter(s) is equavalent to:
            smap = {}
            for c in s:
                smap[c] = smap.get(c, 0) + 1
        '''
        tmap = Counter(t)
        # print(smap)
        # print(tmap)

        '''
        this is how to loop over a map in python
        1. for c in smap -> loop over kol il keys
        2. for key, val in smap.items() -> bnlf 3la kol il keys wel values
        3. for val in smap.values() -> btlf 3la kol il values
        '''

        '''
            smap == tmap -> is equavalent to:
            for c, freq in smap.items():
                if tmap[c] != freq:
                    return False
            return True
        '''
        
        return smap==tmap

        
        