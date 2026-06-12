from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        mymap = {}
        for strr in strs:
            key = tuple(sorted(Counter(strr).items()))
            if key not in mymap:
                mymap[key] = []
            mymap[key].append(strr)

        output =[]
        for val in mymap.values():
            output.append(val)

        return output