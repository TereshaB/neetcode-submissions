class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        prefix_sum=0
        check={0:1}
        for n in nums: 
            prefix_sum+=n
            if(prefix_sum-k in check):
                count+=check[prefix_sum-k]
            check[prefix_sum]=check.get(prefix_sum,0)+1
        return count 
        


        