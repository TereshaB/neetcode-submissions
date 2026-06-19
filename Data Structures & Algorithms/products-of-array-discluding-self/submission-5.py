#optimized soln 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))
        prefix =1
        for i in range(len(nums)): #prefix 
            res[i]=prefix 
            prefix*=nums[i]
        postfix=1
        for i in range((len(nums)-1),-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
    #O(1)space complexity as output array doesn't count as extra memory
    #O(n) time 
    # no division operator used 



   



























