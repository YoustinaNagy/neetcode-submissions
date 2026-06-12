class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for s in strs:
            s_sorted = sorted(s)
            s_sorted_str = ''.join(s_sorted)
            lst = mp.get(s_sorted_str, [])
            lst.append(s)
            mp[s_sorted_str] = lst 
        
        return list(mp.values())