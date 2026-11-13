class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=len(nums)
        tot=0
        arr_sum=0
        for i in range(num+1):
            tot+=i
        for i in range(num):
            arr_sum+=nums[i]
        res=tot-arr_sum
        return res

        