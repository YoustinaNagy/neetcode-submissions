class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            for c in word:
                res=res + str(ord(c)) + "_"
            res=res+"/"
        
        # print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        strs= s.split('/')
        res =[]
        # print (strs)
        for w in range(len(strs)-1):
            word=strs[w]
            chars=word.split('_')
            decoded=""
            for ch in range(len(chars)-1):
                c=chars[ch]
                if len(c)>0:
                    decoded += chr(int(c))
            
            res.append(decoded)
        # if len(res)==0 : res.append("")
        return res




