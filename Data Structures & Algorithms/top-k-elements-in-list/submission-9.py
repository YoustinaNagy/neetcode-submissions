class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # return [num for num, _ in count.most_common(k)]


        # print(count.items())
        # print(type(count.items()))//list of tuple 

        count = Counter(nums)
        sortedlst= sorted( count.items() , key=lambda x:x[1] , reverse=True)
        # print(sortedlst)
        # return[]
        return[item[0] for _,item in enumerate(sortedlst[:k]) ]

        # count = Counter(nums)
        # lst = enumerate(count)
        # lst=sorted(lst, key=lambda x:x[1] ,reverse=True)
        # print(lst)
        # res=[]
        # for i in range(k):
        #     res.append(lst[i][1])
        # return res
        