class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        res=[]
        for s in strs:
            count = Counter(s)
            add = True
            for key , value in dictt.items():
                if count == value:
                    res[key].append(s)
                    add= False
                    break;
            if add:
                dictt[len(res)]= count
                lst = [s]
                res.append(lst)
        return res















        # mp = {}

        # for s in strs:
        #     s_sorted = sorted(s)
        #     s_sorted_str = ''.join(s_sorted)
        #     lst = mp.get(s_sorted_str, [])
        #     lst.append(s)
        #     mp[s_sorted_str] = lst 
        
        # return list(mp.values())