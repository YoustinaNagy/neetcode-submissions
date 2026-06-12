class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter = Counter(nums)
        most_common = myCounter.most_common(k)
        return [key for key, _ in most_common]
        # cmap = sorted(myCounter.items(), key=lambda item: item[1], reverse=True)

        # print(myCounter)
        # print(myCounter.items()) # [(1, 1), (2, 2), (3, 3)]
        # print(sorted(myCounter.items(), key=lambda item: item[1], reverse=True))

        # output =[]
        # i=0;
        # for c in cmap:
        #     if(i<k):
        #         output.append(c[0])
        #     i+=1;
        # return output
        