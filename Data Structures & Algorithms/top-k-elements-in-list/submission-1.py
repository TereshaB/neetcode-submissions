class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for i in nums:
            counter[i]=1+counter.get(i,0)
        heap =[]
        for i in counter.keys():
            heapq.heappush(heap,(counter[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range (k):
            res.append(heapq.heappop(heap)[1])
        return res