class Solution:

    def encode(self, strs: List[str]) -> str:
        # handle empty string case 
        if not strs:
            return ""



        res = ""
        for s in strs:
            res += str(len(s))
            res += ','

        res += '#'
        for s in strs:
            res += s
        return res
    

    def decode(self, s: str) -> List[str]:
        # ["Hello","World"] -> sizes = [5, 5]
        
        # 5,5,#HelloWorld
        if s == '':
            return []
        
        idx = s.find('#')
        first_part = s[:idx-1] # slicing -> pretty easy in python s[start:end:increment/reverse]
        second_part = s[idx+1:]

        sizes = [int(x) for x in first_part.split(',')] # list comprehension
        # sizes = []
        # for x in first_part.split(','):
        #     sizes.append(int(x))
        res = []
        i = 0
        for size in sizes:
            word = second_part[i:i+size]
            res.append(word)
            i += size
        return res


        
        
            


