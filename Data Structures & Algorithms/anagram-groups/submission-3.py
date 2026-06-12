class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            dictt[tuple(count)].append(word)
        return list(dictt.values())
        # dictt = {}
        # res=[]
        # for s in strs:
        #     count = Counter(s)
        #     add = True
        #     for key , value in dictt.items():
        #         if count == value:
        #             res[key].append(s)
        #             add= False
        #             break;
        #     if add:
        #         dictt[len(res)]= count
        #         lst = [s]
        #         res.append(lst)
        # return res















        # mp = {}

        # for s in strs:
        #     s_sorted = sorted(s)
        #     s_sorted_str = ''.join(s_sorted)
        #     lst = mp.get(s_sorted_str, [])
        #     lst.append(s)
        #     mp[s_sorted_str] = lst 
        
        # return list(mp.values())